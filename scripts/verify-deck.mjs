import { chromium } from '@playwright/test'
import fs from 'node:fs/promises'
import path from 'node:path'
import vm from 'node:vm'

const base = (process.argv[2] || 'http://localhost:4173').replace(/\/$/, '')
const root = path.resolve(import.meta.dirname, '..')
const output = path.join(root, '.qa')
await fs.mkdir(path.join(output, 'screenshots'), { recursive: true })
const edge = process.env.PLAYWRIGHT_EXECUTABLE_PATH || 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
const browser = await chromium.launch({ executablePath: edge, headless: true })
const context = await browser.newContext({ viewport: { width: 1280, height: 720 }, reducedMotion: 'reduce' })
const page = await context.newPage()
const errors = [], external = new Set(), failures = []
page.on('pageerror', e => errors.push(e.message))
page.on('console', m => {if(m.type()==='error') errors.push(m.text())})
page.on('response', r => {if(r.url().startsWith(base)&&r.status()>=400) errors.push(`HTTP ${r.status()}: ${r.url()}`)})
page.on('request', r => { if (/^https?:/.test(r.url()) && !r.url().startsWith(base)) external.add(r.url()) })
const results = []
const clean = s => s.normalize('NFKC').replace(/Gaisb�ck/g,'Gaisböck').replace(/�/g,'±').replace(/[^\p{L}\p{N}±%<>≥=]/gu,'').toLowerCase()
const source = JSON.parse(await fs.readFile(path.join(root, 'reference/source-text.json'), 'utf8'))
const manifest = JSON.parse(await fs.readFile(path.join(root, 'slide-manifest.json'), 'utf8'))
const imageUses = new Map()
const protectedContent=JSON.parse(await fs.readFile(path.join(root,'reference/protected-table-content.json'),'utf8'))
const differentialSource=await fs.readFile(path.join(root,'components/DifferentialTable.vue'),'utf8')
for(const name of ['bands','headers']) {
  const expression=differentialSource.match(name==='bands'?/const bands = (\[[\s\S]*?\n\])/:/const headers = (\[[^\n]+\])/)[1]
  if(JSON.stringify(vm.runInNewContext(expression))!==JSON.stringify(protectedContent[name])) throw new Error(`Protected differential ${name} changed`)
}
if(manifest.length!==36 || manifest.filter(m=>m.kind==='source').length!==source.slides.length || manifest.filter(m=>m.kind==='diagram').length!==5 || manifest.filter(m=>m.kind==='microscopy').length!==3) throw new Error('Manifest does not match the approved 36-slide structure')
if(manifest.filter(m=>m.kind==='source').some((m,i)=>m.sourceSlide!==i+1)) throw new Error('Original source slide order changed')
if(manifest.some(m=>!m.chapter||typeof m.artwork!=='string'||typeof m.illustrationCredit!=='boolean')) throw new Error('Atlas chapter/artwork metadata missing')
// These source sentences are represented by tables or split title/section labels.
// Check every meaningful segment instead of requiring the original prose order.
const structural = {
  5: { index:2, required:['Healthy adult man','16 g/dL ± 2 g/dL','47% ± 6%','Menstruating adult woman','Usually','13 g/dL ± 2 gm/dL','40% ± 6%'] },
  10:{index:1,required:['Absolute SECONDARY erythrocytosis','High serum EPO levels','PART 2-2']},
  14:{index:1,required:['Absolute SECONDARY erythrocytosis','Neonatal Polycythemia','PART 2-3']},
  15:{index:0,required:['PART 3','Absolute hereditary / congenital erythrocytosis']},
  17:{index:0,required:['PART 4','PV: absolute primary acquired erythrocytosis']},
}

try {
  for (const entry of manifest) {
    const slide=entry.position
    const states=Array.from({length:entry.clicks+1},(_,i)=>i)
    let allText = ''
    for (const clicks of states) {
      await page.goto(`${base}/${slide}?clicks=${clicks}`, { waitUntil:'networkidle' })
      await page.evaluate(() => document.fonts.ready)
      const layout = page.locator('.slidev-layout:visible').first()
      await layout.waitFor()
      const result = await layout.evaluate(el => {
        const box = el.getBoundingClientRect(), scale = box.width / 1280
        const overflow = []
        const walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT)
        while (walk.nextNode()) {
          const node = walk.currentNode, parent = node.parentElement
          if (!node.textContent.trim() || !parent || parent.closest('footer,svg,.slidev-vclick-hidden,[aria-hidden="true"]')) continue
          if (!parent.getBoundingClientRect().width || getComputedStyle(parent).visibility === 'hidden') continue
          const range = document.createRange(); range.selectNodeContents(node)
          const r = range.getBoundingClientRect()
          const b = (r.bottom-box.top)/scale, right=(r.right-box.left)/scale, left=(r.left-box.left)/scale
          if (b>671 || right>1228 || left<44) overflow.push({text:node.textContent.trim().slice(0,90),bottom:Math.round(b),right:Math.round(right),left:Math.round(left)})
        }
        return { text:el.innerText, overflow, font:getComputedStyle(el).fontFamily, fontLoaded:document.fonts.check('28px "Source Sans 3"'), images:[...el.querySelectorAll('img')].map(i=>({src:i.getAttribute('src'),ok:i.complete&&i.naturalWidth>0})), svgImages:[...el.querySelectorAll('svg image')].map(i=>i.getAttribute('href')||i.getAttribute('xlink:href')), scrollHeight:el.scrollHeight }
      })
      await layout.screenshot({ path:path.join(output, 'screenshots', `slide-${String(slide).padStart(2,'0')}-${clicks}.png`), animations:'disabled' })
      allText += '\n'+result.text
      results.push({ slide, id:entry.id, sourceSlide:entry.sourceSlide, clicks, ...result })
      if (result.overflow.length) failures.push(`Slide ${slide}/${clicks}: ${result.overflow.length} geometry issue(s)`)
      if (result.images.some(x=>!x.ok)) failures.push(`Slide ${slide}: image failed`)
      if(!result.fontLoaded) failures.push(`Slide ${slide}: local font not loaded`)
      const usesServier=[...result.images.map(i=>i.src),...result.svgImages].some(s=>s?.startsWith('/art/atlas/'))
      if(usesServier&&!entry.illustrationCredit) failures.push(`Slide ${slide}: illustration attribution missing`)
      for(const href of result.svgImages.filter(h=>h?.startsWith('/'))) {try{await fs.access(path.join(root,'public',href))}catch{failures.push(`Missing SVG-linked illustration: ${href}`)}}
      if(clicks===0) for(const im of result.images.filter(x=>x.src?.startsWith('/images/ash-'))) imageUses.set(im.src,(imageUses.get(im.src)||0)+1)
    }
    const sourceSlide=entry.sourceSlide
    const paragraphs = sourceSlide ? source.slides[sourceSlide-1].paragraphs : []
    const missing = paragraphs.filter((p,i) => p.trim().length>45 && i!==structural[sourceSlide]?.index && !clean(allText).includes(clean(p)))
    for(const expected of structural[sourceSlide]?.required || []) if(!clean(allText).includes(clean(expected))) missing.push(expected)
    const protectedHtml=sourceSlide===20?protectedContent.criteriaHtml:sourceSlide===26?protectedContent.treatmentHtml:[]
    for(const html of protectedHtml) {
      const text=await page.evaluate(html=>{const e=document.createElement('div');e.innerHTML=html;return e.textContent},html)
      if(!clean(allText).includes(clean(text))) missing.push(text)
    }
    if (missing.length) results.push({slide,sourceTextNeedsReview:missing})
  }
  // Verify real keyboard progression, not just query-driven component rendering.
  for (const entry of manifest.filter(m=>m.clicks>0)) {
    const slide=entry.position
    await page.goto(`${base}/${slide}?clicks=0`,{waitUntil:'networkidle'})
    for(let click=1;click<=entry.clicks;click++) {
      await page.keyboard.press('ArrowRight')
      await page.waitForURL(u=>u.pathname===`/${slide}`&&Number(u.searchParams.get('clicks')||0)===click)
    }
    for(let click=entry.clicks-1;click>=0;click--) {
      await page.keyboard.press('ArrowLeft')
      await page.waitForURL(u=>u.pathname===`/${slide}`&&Number(u.searchParams.get('clicks')||0)===click)
    }
    await page.keyboard.press('Space')
    await page.waitForURL(u=>u.pathname===`/${slide}`&&u.searchParams.get('clicks')==='1')
    await page.goto(`${base}/${slide+1}`,{waitUntil:'networkidle'})
    await page.goto(`${base}/${slide}?clicks=0`,{waitUntil:'networkidle'})
    if(new URL(page.url()).searchParams.get('clicks')!=='0') failures.push(`State did not reset: ${entry.id}`)
  }
  for(const image of ['60160','60161','60162','60164']) if(imageUses.get(`/images/ash-${image}.jpg`)!==1) failures.push(`ASH ${image} must appear exactly once`)
  for (const route of ['/overview','/presenter/27']) {
    const response=await page.goto(base+route,{waitUntil:'networkidle'})
    if(response.status()!==200) failures.push(`Route failed: ${route}`)
    await page.screenshot({path:path.join(output,route.includes('presenter')?'presenter.png':'overview.png')})
  }
  // Check actual motion settles and can reverse in the full-motion mode too.
  const motionPage=await browser.newPage({viewport:{width:1280,height:720},reducedMotion:'no-preference'})
  motionPage.on('pageerror',e=>errors.push(e.message))
  motionPage.on('console',m=>{if(m.type()==='error')errors.push(m.text())})
  motionPage.on('request',r=>{if(/^https?:/.test(r.url())&&!r.url().startsWith(base))external.add(r.url())})
  await fs.mkdir(path.join(output,'motion-states'),{recursive:true})
  for(const entry of manifest) {
    for(let click=0;click<=entry.clicks;click++) {
      await motionPage.goto(`${base}/${entry.position}?clicks=${click}`,{waitUntil:'networkidle'})
      await motionPage.evaluate(()=>document.fonts.ready)
      await motionPage.waitForTimeout(800)
      const layout=motionPage.locator('.slidev-layout:visible').first()
      const unfinished=await layout.evaluate(el=>el.getAnimations({subtree:true}).filter(a=>a.playState==='running'||a.playState==='pending').length)
      if(unfinished)failures.push(`Motion did not settle: ${entry.id}/${click}`)
      await layout.screenshot({path:path.join(output,'motion-states',`slide-${String(entry.position).padStart(2,'0')}-${click}.png`)})
    }
    if(entry.clicks) {
      for(let click=entry.clicks-1;click>=0;click--) {
        await motionPage.keyboard.press('ArrowLeft')
        await motionPage.waitForURL(u=>u.pathname===`/${entry.position}`&&Number(u.searchParams.get('clicks')||0)===click)
      }
      // Change direction while transitions are running. No timers may overwrite the requested state.
      await motionPage.keyboard.press('Space');await motionPage.keyboard.press('ArrowLeft');await motionPage.keyboard.press('ArrowRight')
      await motionPage.waitForURL(u=>u.pathname===`/${entry.position}`&&Number(u.searchParams.get('clicks')||0)===1)
      await motionPage.waitForTimeout(800)
      await motionPage.keyboard.press('ArrowLeft')
      await motionPage.waitForURL(u=>u.pathname===`/${entry.position}`&&Number(u.searchParams.get('clicks')||0)===0)
    }
    console.log(`Full-motion review: ${entry.position}/${manifest.length}`)
  }
  await motionPage.close()
  await fs.writeFile(path.join(output,'report.json'),JSON.stringify({base,results,errors,external:[...external],failures,imageUses:Object.fromEntries(imageUses)},null,2))
  console.log(JSON.stringify({renderedStates:results.filter(x=>'clicks'in x).length,errors,external:[...external],failures,sourceReview:results.filter(x=>x.sourceTextNeedsReview).map(x=>({slide:x.slide,paragraphs:x.sourceTextNeedsReview}))},null,2))
  if(errors.length || failures.length || external.size || results.some(x=>x.sourceTextNeedsReview)) process.exitCode=1
} finally { await browser.close() }

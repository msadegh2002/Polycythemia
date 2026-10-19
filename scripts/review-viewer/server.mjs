import http from 'node:http'
import fs from 'node:fs/promises'
import { createReadStream } from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { randomBytes } from 'node:crypto'
import { spawn } from 'node:child_process'
import { tmpdir } from 'node:os'

const home = path.dirname(fileURLToPath(import.meta.url))
const root = path.resolve(home, '../presentation')
const token = randomBytes(24).toString('hex')
const clients = new Map()
const started = Date.now()
let stopTimer, stopping = false
const clientScript = (await fs.readFile(path.join(home, 'client.js'), 'utf8')).replace('__VIEWER_TOKEN__', JSON.stringify(token))
const indexHtml = (await fs.readFile(path.join(root, 'index.html'), 'utf8')).replace('</head>', '<script src="/__review/client.js"></script></head>')
const mime = { '.html':'text/html; charset=utf-8', '.js':'text/javascript; charset=utf-8', '.mjs':'text/javascript; charset=utf-8', '.css':'text/css; charset=utf-8', '.json':'application/json; charset=utf-8', '.svg':'image/svg+xml', '.png':'image/png', '.jpg':'image/jpeg', '.jpeg':'image/jpeg', '.webp':'image/webp', '.gif':'image/gif', '.ico':'image/x-icon', '.woff2':'font/woff2', '.woff':'font/woff', '.ttf':'font/ttf', '.wasm':'application/wasm' }

function respond(res, status, type, body, head=false) {
  res.writeHead(status, { 'Content-Type':type, 'Cache-Control':'no-cache', 'X-Content-Type-Options':'nosniff', 'Content-Length':Buffer.byteLength(body) })
  res.end(head ? undefined : body)
}
function keepOpen() { clearTimeout(stopTimer) }
function closeSoon() {
  keepOpen()
  if (!clients.size) stopTimer=setTimeout(stop, 2500)
}
async function stop() {
  if(stopping) return
  stopping=true
  clearTimeout(stopTimer)
  clearInterval(cleanup)
  server.close(()=>process.exit(0))
  server.closeIdleConnections()
  setTimeout(()=>process.exit(0),1500).unref()
}

const server = http.createServer(async (req,res) => {
  try {
    const url=new URL(req.url, 'http://127.0.0.1')
    if(url.pathname==='/__review/health') return respond(res,200,'application/json',JSON.stringify({viewer:'polycythemia',pid:process.pid}))
    if(url.pathname==='/__review/client.js') return respond(res,200,mime['.js'],clientScript)
    if(url.pathname==='/__review/ping' && req.method==='POST') {
      let body=''
      for await (const chunk of req) {body+=chunk; if(body.length>2048) return respond(res,413,'text/plain','Request too large')}
      let data
      try {data=JSON.parse(body)} catch {return respond(res,400,'text/plain','Invalid request')}
      if(data.token!==token || typeof data.id!=='string' || data.id.length>100) return respond(res,403,'text/plain','Forbidden')
      keepOpen()
      if(data.closed) {clients.delete(data.id);closeSoon()} else clients.set(data.id,Date.now())
      return respond(res,200,'text/plain','OK')
    }
    if(req.method!=='GET' && req.method!=='HEAD') return respond(res,405,'text/plain','Method not allowed')
    const file=path.resolve(root,decodeURIComponent(url.pathname).replace(/^\/+/,''))
    if(file!==root && !file.startsWith(root+path.sep)) return respond(res,403,'text/plain','Forbidden')
    let stat
    try {stat=await fs.stat(file)} catch {}
    if(!stat?.isFile() || path.basename(file)==='index.html') {
      if(path.extname(url.pathname) && path.basename(file)!=='index.html') return respond(res,404,'text/plain','Not found')
      keepOpen()
      return respond(res,200,mime['.html'],indexHtml,req.method==='HEAD')
    }
    res.writeHead(200,{'Content-Type':mime[path.extname(file).toLowerCase()]||'application/octet-stream','Content-Length':stat.size,'Cache-Control':'private, max-age=3600','X-Content-Type-Options':'nosniff'})
    if(req.method==='HEAD') return res.end()
    createReadStream(file).on('error',()=>res.destroy()).pipe(res)
  } catch {if(!res.headersSent) respond(res,400,'text/plain','Unable to read request'); else res.destroy()}
})
server.requestTimeout=15000
server.headersTimeout=15000
server.on('error', async error=>{
  await fs.writeFile(path.join(tmpdir(),'polycythemia-viewer-error.log'),String(error)).catch(()=>{})
  process.exit(1)
})
const cleanup=setInterval(()=>{
  for(const [id,time] of clients) if(Date.now()-time>10*60*1000) clients.delete(id)
  if(!clients.size && Date.now()-started>10*60*1000) closeSoon()
},60000)
process.on('SIGINT',stop)
process.on('SIGTERM',stop)
server.listen(0,'127.0.0.1',async()=>{
  const url=`http://127.0.0.1:${server.address().port}/1`
  if(process.env.PRESENTATION_VIEWER_STATE) await fs.writeFile(process.env.PRESENTATION_VIEWER_STATE,JSON.stringify({url,pid:process.pid}))
  if(process.env.PRESENTATION_VIEWER_NO_OPEN!=='1') {
    const powershell=path.join(process.env.SystemRoot||'C:\\Windows','System32','WindowsPowerShell','v1.0','powershell.exe')
    const child=spawn(powershell,['-NoProfile','-NonInteractive','-WindowStyle','Hidden','-Command',`Start-Process '${url}'`],{windowsHide:true,stdio:'ignore'})
    child.on('error',()=>{})
  }
})

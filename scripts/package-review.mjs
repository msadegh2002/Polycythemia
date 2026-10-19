import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { execFileSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'

const project=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
if(process.platform!=='win32'||process.arch!=='x64')throw new Error('Generate the portable Windows review ZIP on 64-bit Windows; the bundled runtime must match the recipient platform.')
const stage=path.join(project,'output','review',String(Date.now()),'Polycythemia-Review')
const viewer=path.join(stage,'viewer')
const archive=path.join(project,'..','Polycythemia-Review.zip')
await fs.access(path.join(project,'dist/index.html'))
await fs.mkdir(viewer,{recursive:true})
await fs.cp(path.join(project,'dist'),path.join(stage,'presentation'),{recursive:true})
await fs.copyFile(process.execPath,path.join(viewer,'node.exe'))
for(const file of ['server.mjs','client.js']) await fs.copyFile(path.join(project,'scripts/review-viewer',file),path.join(viewer,file))
for(const file of ['Open Presentation.cmd','Read me.txt']) {
  const text=await fs.readFile(path.join(project,'scripts/review-viewer',file),'utf8')
  await fs.writeFile(path.join(stage,file),text.replace(/\r?\n/g,'\r\n'))
}
const licenseUrl=`https://raw.githubusercontent.com/nodejs/node/${process.version}/LICENSE`
const response=await fetch(licenseUrl)
if(!response.ok)throw new Error(`Node license download failed: ${response.status}`)
const license=await response.text()
if(!license.includes('Copyright Node.js contributors.')||license.length<100000)throw new Error('Incomplete Node license')
await fs.writeFile(path.join(viewer,'NODE-LICENSE.txt'),license)
await fs.copyFile(path.join(project,'ASSET-CREDITS.md'),path.join(viewer,'ASSET-CREDITS.md'))

// Keep dependency notices with the portable build, outside the reviewer's opening flow.
async function collectNotices(dir,relative='') {
  const result=[]
  for(const entry of await fs.readdir(dir,{withFileTypes:true})) {
    if(entry.isDirectory()) result.push(...await collectNotices(path.join(dir,entry.name),path.join(relative,entry.name)))
    else if(entry.isFile()&&/^(licen[cs]e|copying|notice|ofl)(?:[._-].*)?$/i.test(entry.name)) {
      const source=path.join(dir,entry.name),destination=path.join(viewer,'dependency-notices',relative,entry.name)
      await fs.mkdir(path.dirname(destination),{recursive:true});await fs.copyFile(source,destination)
      result.push(path.join(relative,entry.name))
    }
  }
  return result
}
const notices=await collectNotices(path.join(project,'node_modules'))
await fs.writeFile(path.join(viewer,'dependency-notices.json'),JSON.stringify(notices,null,2))
const hash=data=>createHash('sha256').update(data).digest('hex')
const files=[]
async function inventory(dir) {
  for(const e of await fs.readdir(dir,{withFileTypes:true})) {
    const p=path.join(dir,e.name)
    if(e.isDirectory())await inventory(p)
    else if(e.isFile()) {const data=await fs.readFile(p);files.push({path:path.relative(stage,p).replaceAll('\\','/'),bytes:data.length,sha256:hash(data)})}
  }
}
await inventory(stage)
await fs.writeFile(path.join(viewer,'build-info.json'),JSON.stringify({node:process.version,architecture:process.arch,nodeLicenseSource:licenseUrl,files},null,2))
execFileSync('python',['-X','utf8','-c',`import pathlib,zipfile,sys
root=pathlib.Path(sys.argv[1])
with zipfile.ZipFile(sys.argv[2],'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(root.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(root).as_posix())
`,stage,archive],{stdio:'inherit'})
const archiveBytes=(await fs.stat(archive)).size
await fs.mkdir(path.join(project,'.qa'),{recursive:true})
await fs.writeFile(path.join(project,'.qa/review-package.json'),JSON.stringify({stage,archive,archiveBytes,files:files.length,node:process.version},null,2))
console.log(JSON.stringify({stage,archive,megabytes:Math.round(archiveBytes/1024/1024*10)/10,files:files.length}))

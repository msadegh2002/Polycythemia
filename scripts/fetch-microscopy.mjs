import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createHash } from 'node:crypto'

const project=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
const args=process.argv.slice(2)
const checkOnly=args.includes('--check')
const destinationIndex=args.indexOf('--destination')
if(destinationIndex>=0&&!args[destinationIndex+1])throw new Error('--destination requires a directory')
const destination=destinationIndex>=0?path.resolve(args[destinationIndex+1]):project
const assets=JSON.parse(await fs.readFile(path.join(project,'reference/microscopy-assets.json'),'utf8'))
const sha=data=>createHash('sha256').update(data).digest('hex')

async function restore(asset) {
  const file=path.join(destination,asset.path)
  let existing
  try {existing=await fs.readFile(file)} catch(error) {if(error.code!=='ENOENT')throw error}
  if(existing) {
    if(sha(existing)!==asset.sha256)throw new Error(`ASH ${asset.id}: existing image differs from the recorded source; review it before replacing it`)
    return 'present'
  }
  if(checkOnly)throw new Error(`Missing ${asset.path}; run npm run assets:fetch`)
  let failure
  for(let attempt=0;attempt<3;attempt++) {
    try {
      const response=await fetch(asset.download,{signal:AbortSignal.timeout(45000)})
      if(!response.ok)throw new Error(`HTTP ${response.status}`)
      const data=Buffer.from(await response.arrayBuffer())
      if(sha(data)!==asset.sha256)throw new Error('Downloaded image does not match the recorded original')
      await fs.mkdir(path.dirname(file),{recursive:true})
      await fs.writeFile(file,data,{flag:'wx'})
      console.log(`Restored ASH image ${asset.id}`)
      return 'downloaded'
    } catch(error) {failure=error;if(attempt<2)await new Promise(resolve=>setTimeout(resolve,1000*(attempt+1)))}
  }
  throw new Error(`Could not restore ASH ${asset.id}: ${failure.message}. Retry npm run assets:fetch when the source is reachable.`)
}

const results=await Promise.allSettled(assets.map(restore))
const failures=results.filter(result=>result.status==='rejected')
if(failures.length) {
  for(const failure of failures)console.error(failure.reason.message)
  process.exitCode=1
} else console.log(`Microscopy assets verified: ${assets.length}. See ASSET-CREDITS.md for usage and attribution.`)

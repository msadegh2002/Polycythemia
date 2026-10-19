(() => {
  const token = __VIEWER_TOKEN__
  const id = crypto.randomUUID()
  const report = closed => {
    const body = JSON.stringify({ token, id, closed })
    if (!navigator.sendBeacon('/__review/ping', new Blob([body], {type:'text/plain'})))
      fetch('/__review/ping', {method:'POST',body,keepalive:true}).catch(()=>{})
  }
  report(false)
  const heartbeat=setInterval(()=>report(false),20000)
  addEventListener('pageshow',()=>report(false))
  addEventListener('pagehide',()=>{clearInterval(heartbeat);report(true)})
})()

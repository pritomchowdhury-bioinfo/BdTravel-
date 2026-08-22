
const CACHE='bdtravel-core-v1';
const CORE=['./','./index.html','./data/districts-64.json','./data/tourist-spots-64.json','./data/emergency-bangladesh.json','./data/emergency-helplines.json'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{
 if(e.request.method!=='GET')return;
 e.respondWith(caches.match(e.request).then(cached=>cached||fetch(e.request).then(r=>{
   if(e.request.url.startsWith(self.location.origin)){const copy=r.clone();caches.open(CACHE).then(c=>c.put(e.request,copy));}
   return r;
 }).catch(()=>cached||new Response('Offline — cached BDTravel content is available.',{status:503,headers:{'Content-Type':'text/plain'}}))));
});

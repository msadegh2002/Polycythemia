<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
const props=withDefaults(defineProps<{compact?:boolean;fixed?:string}>(),{compact:false,fixed:''})
const {$clicks}=useSlideContext()
const phase=computed(()=>props.fixed==='relative'?2:props.fixed==='absolute'?1:$clicks.value)
const samples=computed(()=>props.compact?[
 {id:'normal',x:115,label:'Normal',sub:'Red-cell mass / plasma volume',plasma:70,cells:44,width:135},
 {id:'relative',x:445,label:'Relative',sub:'Reduced plasma volume',plasma:36,cells:44,width:135},
]:[
 {id:'normal',x:110,label:'Normal',sub:'Red-cell mass / plasma volume',plasma:142,cells:86,width:200},
 {id:'absolute',x:475,label:'Absolute erythrocytosis',sub:'Increased red-cell mass',plasma:142,cells:phase.value>=1?146:86,width:200},
 {id:'relative',x:840,label:'Relative erythrocytosis',sub:'Reduced plasma volume',plasma:phase.value>=2?70:142,cells:86,width:200},
])
const bottom=computed(()=>props.compact?134:320)
const active=(id:string)=>props.compact||id==='normal'||(id==='absolute'&&phase.value>=1)||(id==='relative'&&phase.value>=2)
</script>
<template>
  <div class="blood-volume" :class="{compact}">
    <svg :viewBox="compact?'0 0 700 205':'0 0 1152 435'" role="img" aria-label="Schematic comparison: absolute erythrocytosis increases red-cell mass; relative erythrocytosis reduces plasma volume while red-cell mass stays the same.">
      <g v-for="s in samples" :key="s.id" class="sample" :class="{active:active(s.id)}">
        <rect :x="s.x-4" :y="compact?14:20" :width="s.width+8" :height="compact?126:306" rx="20" fill="#fdfcfa" stroke="var(--figure-line)" stroke-width="2" />
        <rect :x="s.x" :y="bottom-s.cells-s.plasma" :width="s.width" :height="s.plasma" rx="16" fill="#ead5bf" class="fluid" />
        <rect :x="s.x" :y="bottom-s.cells" :width="s.width" :height="s.cells" rx="14" fill="#8f2737" class="fluid" />
        <g v-for="j in (s.cells>100?20:12)" :key="j" class="diagram-cell" :style="{transform:`translate(${s.x+22+((j-1)%4)*(s.width-44)/3}px,${bottom-15-Math.floor((j-1)/4)*(compact?11:25)}px)`}">
          <image href="/art/atlas/erythrocyte.svg" :x="compact?-12:-18" :y="compact?-8:-12" :width="compact?24:36" :height="compact?16:24" />
        </g>
        <text :x="s.x+s.width/2" :y="compact?164:365" text-anchor="middle" class="sample-label">{{s.label}}</text>
        <text :x="s.x+s.width/2" :y="compact?188:396" text-anchor="middle" class="sample-sub">{{s.sub}}</text>
      </g>
      <text x="8" :y="compact?52:134" class="legend">Plasma</text><text x="8" :y="compact?116:291" class="legend red">Red cells</text>
    </svg>
    <div v-if="!compact" class="volume-caption"><span class="stage-dot" v-for="i in 3" :key="i" :class="{on:phase>=i-1}"></span><span>Schematic · no quantitative scale</span></div>
  </div>
</template>
<style scoped>
.blood-volume{height:465px;position:relative}.blood-volume svg{width:100%;height:435px;overflow:visible;font-family:'Source Sans 3',sans-serif}.sample-label{font-size:27px;font-weight:600;fill:var(--ink);transition:fill 280ms}.sample.active .sample-label{fill:var(--wine)}.sample-sub{font-size:22px;fill:var(--muted)}.legend{font-size:21px;fill:var(--muted)}.legend.red{fill:var(--wine)}.fluid{transition:y 650ms var(--figure-ease),height 650ms var(--figure-ease)}.diagram-cell{transition:transform 600ms var(--figure-ease),opacity 600ms}.volume-caption{display:flex;align-items:center;justify-content:center;gap:9px;color:var(--muted);font-size:17px;margin-top:5px}.volume-caption>span:last-child{margin-left:10px}.stage-dot{width:6px;height:6px;border-radius:50%;background:#d8c5c2}.stage-dot.on{background:var(--wine)}.compact{height:190px}.compact svg{height:190px}.compact .sample-label{font-size:25px}.compact .sample-sub{font-size:18px}.compact .legend{font-size:17px}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
</style>

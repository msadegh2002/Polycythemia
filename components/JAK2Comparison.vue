<script setup lang="ts">
import { useFigureStep } from '../composables/useFigureStep'
const { step } = useFigureStep(3)
const lanes = [
  { tag:'HIGH EPO LEVELS', title:'EPO-driven erythropoiesis', art:'erythrocyte', labels:['Cellular hypoxia','Erythropoietin','Erythroid progenitor cells','Erythropoiesis'] },
  { tag:'LOW EPO LEVELS', title:'Autonomous JAK2 signaling', art:'stem-cell', labels:['Hematopoietic stem cell','JAK2 V617F / exon 12','Persistent JAK–STAT signal','Pan myelosis and symptoms'] },
]
</script>
<template>
  <div class="signaling-comparison">
    <section v-for="(lane,index) in lanes" :key="lane.title" class="signal-lane" :class="{active:step>=index+1,focused:step===index+1}">
      <header><span>{{lane.tag}}</span><h2>{{lane.title}}</h2><img :src="`/art/atlas/${lane.art}.svg`" alt="" aria-hidden="true" /></header>
      <svg viewBox="0 0 540 360" role="img" :aria-label="lane.labels.join(', then ')">
        <g v-for="(label,i) in lane.labels" :key="label">
          <rect v-if="i===1" x="67" y="98" width="452" height="56" rx="2" class="signal-emphasis" />
          <circle cx="26" :cy="40+i*90" r="5" class="path-node" :class="{reached:step>=index+1}" />
          <FigureConnector v-if="i<3" :key="`${index}-${i}-${step>=index+1}`" :style="{'--trace-delay':`${i*110}ms`,'--path-duration':'350ms'}" :d="`M26 ${52+i*90}V${114+i*90}`" :active="step>=index+1" :signal="step===index+1" />
          <text x="83" :y="49+i*90" class="signal-label" :class="{emphasis:i===1,output:i===3}">{{label}}</text>
        </g>
      </svg>
    </section>
    <div class="autonomy-summary" :class="{highlighted:step===3}"><span class="summary-rule"></span><p>EPO-independent erythroid colony formation</p></div>
  </div>
</template>
<style scoped>
.signaling-comparison{display:grid;grid-template-columns:1fr 1fr;gap:0 60px;margin-top:12px}
.signal-lane{min-width:0}.signal-lane header{position:relative;padding:18px 70px 18px 0;border-top:2px solid var(--figure-line);transition:border-color 300ms}.signal-lane.active header{border-color:var(--wine)}
header>span{font-size:16px;letter-spacing:.12em;color:var(--muted)}header h2{font-size:28px!important;margin:9px 0 0!important;line-height:1.12!important;min-height:63px}
header img{position:absolute;right:0;top:20px;width:62px;height:70px;object-fit:contain}
svg{width:100%;height:350px}.signal-label{font-size:27px;fill:var(--ink)}.signal-label.emphasis{font-weight:650;fill:var(--wine)}.signal-label.output{font-size:27px;font-weight:650}
.signal-emphasis{fill:#eee8ed;transition:fill 300ms}.active .signal-emphasis{fill:#eadce5}.path-node{fill:var(--paper);stroke:var(--figure-line);stroke-width:2;transition:fill 300ms,stroke 300ms}.path-node.reached{fill:var(--wine);stroke:var(--wine)}
.autonomy-summary{grid-column:1/-1;display:flex;gap:18px;align-items:center;justify-content:flex-end;border-top:1px solid var(--rule);padding:14px 0 0;color:var(--muted);transition:color 300ms}
.autonomy-summary p{font-size:24px!important;margin:0!important}.summary-rule{width:34px;height:2px;background:var(--figure-line);transition:width 300ms,background 300ms}.highlighted{color:var(--wine);font-weight:600}.highlighted .summary-rule{background:var(--wine);width:65px}
</style>

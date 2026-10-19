<script setup lang="ts">
import {useFigureStep} from '../composables/useFigureStep'
const {step}=useFigureStep(3)
const labels=['Hematopoietic stem cell','JAK2 V617F or exon 12','Persistent JAK–STAT signal','Pan myelosis and symptoms']
</script>
<template>
  <div class="jak-pathway-scene">
    <svg class="pathway-links" viewBox="0 0 1152 220" aria-hidden="true"><FigureConnector v-for="(d,i) in ['M210 90H342','M508 90H640','M806 90H915']" :key="i" :d="d" :active="step>=i+1" :signal="step===i+1" /></svg>
    <div v-for="(label,i) in labels" :key="label" class="pathway-step" :class="{visible:i<=step}">
      <svg viewBox="0 0 220 150" role="img" :aria-label="label">
        <image v-if="i===0" href="/art/atlas/stem-cell.svg" x="48" y="5" width="125" height="140" />
        <g v-else-if="i===1"><image href="/art/atlas/stem-cell.svg" x="48" y="5" width="125" height="140"/><rect x="69" y="59" width="82" height="36" rx="18" fill="#85243b"/><text x="110" y="83" text-anchor="middle" style="font-size:21px;fill:white;font-weight:650">JAK2</text></g>
        <g v-else-if="i===2"><circle cx="110" cy="77" r="58" fill="#eee5ee" stroke="#b5a3bb" stroke-width="2"/><text x="110" y="70" text-anchor="middle" fill="#6d5a80" style="font-size:29px;font-weight:650">JAK</text><path d="M84 84H136" stroke="#9b7f9f" stroke-width="1.5"/><text x="110" y="111" text-anchor="middle" fill="#6d5a80" style="font-size:29px;font-weight:650">STAT</text></g>
        <g v-else><image href="/art/atlas/erythrocyte.svg" x="28" y="20" width="93" height="65"/><image href="/art/atlas/neutrophil.svg" x="123" y="20" width="74" height="80"/><image href="/art/atlas/platelet.svg" x="76" y="100" width="31" height="32"/><image href="/art/atlas/platelet.svg" x="118" y="112" width="21" height="22"/></g>
      </svg>
      <h2>{{label}}</h2>
    </div>
  </div>
</template>
<style scoped>
.jak-pathway-scene{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:42px;margin:24px 0 34px;position:relative}.jak-pathway-scene>.pathway-links{position:absolute;inset:0;width:1152px;height:220px;overflow:visible;pointer-events:none}.pathway-step{min-width:0;position:relative}.pathway-step>svg{width:100%;height:180px;overflow:visible;opacity:.48;transition:opacity 300ms}.pathway-step.visible>svg{opacity:1}.pathway-step h2{font-size:27px!important;line-height:1.2!important;text-align:center;max-width:235px;margin:18px auto 0!important;color:var(--ink);transition:color 300ms}.pathway-step.visible h2{color:var(--wine)}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
</style>

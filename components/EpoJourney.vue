<script setup lang="ts">
import {useFigureStep} from '../composables/useFigureStep'
const {step}=useFigureStep(2)
</script>
<template>
  <div class="epo-figure">
    <svg viewBox="0 0 1152 416" role="img" aria-label="Schematic sequence of low oxygen delivery or excess EPO, kidney/tissue signal, and marrow erythropoiesis">
      <text x="158" y="35" text-anchor="middle" class="station-label">Low oxygen delivery</text><text x="158" y="68" text-anchor="middle" class="station-sub">or excess EPO</text>
      <rect x="30" y="141" width="256" height="127" rx="62" fill="#f1e4e9" stroke="#bc8e9f" stroke-width="2"/>
      <path d="M50 156H266M50 253H266" fill="none" stroke="#faf9f6" stroke-width="5"/>
      <g class="vessel-cells"><image v-for="(x,i) in [52,128,204]" :key="i" href="/art/atlas/erythrocyte.svg" :x="x" y="183" width="64" height="45" /></g>
      <FigureConnector d="M311 204H421" :active="step>=1" :signal="true" />
      <image href="/art/atlas/kidney.svg" x="451" y="90" width="136" height="240" />
      <path d="M584 200H624" fill="none" stroke="var(--figure-line)" stroke-width="2"/>
      <circle cx="652" cy="200" r="32" class="epo-signal" :class="{active:step>=1}"/><text x="652" y="208" text-anchor="middle" class="epo-text">EPO</text>
      <text x="556" y="383" text-anchor="middle" class="station-label">Kidney / tissue signal</text>
      <FigureConnector d="M711 204H819" :active="step>=2" :signal="true" />
    </svg>
    <div class="marrow-station" :class="{active:step>=2}"><MarrowIllustration :mixed="false"/><span>Marrow erythropoiesis</span></div>
    <div class="epo-caption"><p>Low oxygen delivery or excess EPO → kidney / tissue signal → marrow erythropoiesis</p><span>Schematic · no quantitative scale</span></div>
  </div>
</template>
<style scoped>
.epo-figure{position:relative;margin-top:16px}.epo-figure>svg{width:1152px;height:416px;overflow:visible}.station-label{font-size:28px;font-weight:600;fill:var(--ink)}.station-sub{font-size:24px;fill:var(--muted)}
.epo-signal{fill:#eee8ee;stroke:var(--figure-line);stroke-width:2;transition:fill 300ms,stroke 300ms}.epo-signal.active{fill:#e4d4df;stroke:var(--wine)}.epo-text{font-size:24px;font-weight:650;fill:var(--wine)}
.marrow-station{position:absolute;right:0;top:31px;width:290px;display:flex;align-items:center;flex-direction:column}.marrow-station :deep(svg){width:240px;height:318px}.marrow-station>span{font-size:27px;font-weight:600;color:var(--ink);margin-top:8px;white-space:nowrap}
.epo-caption{border-top:1px solid var(--rule);padding-top:16px;text-align:center}.epo-caption p{font-size:24px!important;color:var(--muted);margin:0 0 10px!important}.epo-caption>span{font-size:16px;color:var(--muted)}
.vessel-cells{animation:enter-vessel 550ms var(--figure-ease) both}@keyframes enter-vessel{from{transform:translateX(-15px)}to{transform:translateX(0)}}
</style>

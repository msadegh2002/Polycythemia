<script setup lang="ts">
import { computed } from 'vue'
import { useFigureStep } from '../composables/useFigureStep'
const { step } = useFigureStep(4)
const tests = [
  { label:'CBC trend', text:'Confirm persistence; inspect WBC, platelets, MCV and smear.' },
  { label:'Oxygen assessment', text:'Pulse oximetry, sleep study, smoking/CO history, pulmonary and cardiac evaluation when indicated.' },
  { label:'Serum EPO', text:'Usually normal or high in secondary disease; interpret “normal” relative to the degree of erythrocytosis.' },
  { label:'JAK2 testing', text:'Usually absent; if low EPO or the phenotype is strongly suggestive, test JAK2 before closing the case.' },
  { label:'Targeted tests', text:'Medication review, renal/hepatic evaluation, imaging or hereditary work-up according to the history.' },
]
const selected = computed(() => tests[step.value])
</script>
<template>
  <div class="assessment-figure">
    <svg viewBox="0 0 620 432" role="img" aria-label="Five parallel assessment groups, not a diagnostic decision sequence">
      <image href="/art/atlas/specimen.svg" x="52" y="35" width="55" height="300" />
      <text x="80" y="372" text-anchor="middle" class="specimen-label">Blood specimen</text>
      <g v-for="(test,i) in tests" :key="test.label" :class="{selected:i===step}">
        <FigureConnector :d="`M126 190H174V${48+i*77}H240`" :arrow="false" />
        <circle cx="240" :cy="48+i*77" r="3" class="assay-point" />
        <text x="262" :y="57+i*77" class="assay-label">{{test.label}}</text>
        <path :d="`M262 ${77+i*77}H590`" class="assay-rule" />
      </g>
      <FigureConnector :key="step" :d="`M126 190H174V${48+step*77}H240`" active :arrow="false" />
    </svg>
    <aside class="assessment-detail">
      <span class="figure-index">{{String(step+1).padStart(2,'0')}} / 05</span>
      <div :key="step" class="focus-enter"><h2>{{selected.label}}</h2><p>{{selected.text}}</p></div>
    </aside>
  </div>
</template>
<style scoped>
.assessment-figure{display:grid;grid-template-columns:620px 1fr;gap:48px;align-items:center;margin-top:12px}
svg{width:620px;height:432px;overflow:visible}.specimen-label{font-size:20px;fill:var(--muted)}
.assay-label{font-size:27px;font-weight:550;fill:var(--ink);transition:fill 250ms}.selected .assay-label{fill:var(--wine);font-weight:650}
.assay-rule{fill:none;stroke:var(--rule);stroke-width:1}.assay-point{fill:var(--figure-line)}.selected .assay-point{fill:var(--wine)}
.assessment-detail{border-left:1px solid var(--rule);padding:12px 0 12px 34px;min-height:292px}
.figure-index{font-size:17px;letter-spacing:.12em;color:var(--violet);display:block;margin-bottom:25px}
.assessment-detail h2{font-size:37px!important;line-height:1.12!important;margin-bottom:24px!important}
.assessment-detail p{font-size:29px;line-height:1.34;margin-bottom:0!important}
</style>

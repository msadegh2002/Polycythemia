<script setup lang="ts">
import { computed } from 'vue'
import { useFigureStep } from '../composables/useFigureStep'
const { step, printing } = useFigureStep(6)
const headers = ['Variable', 'Causes', 'Associated clinical and/or laboratory features', 'Investigations required for diagnosis or assessment', 'Management']
// Column groups follow the source table's visual ordering. Do not infer new row associations.
const bands = [
  ['Secondary polycythemia',
    'Chronic hypoxia\n  High-altitude abode\n  OSA\nHypoventilation (eg Pickwickian syndrome)\n  Chronic lung disease\n  Cyanotic congenital heart disease\n  Cigarette smoking\n  Hookah smoking',
    'O₂ saturation <92%\nObesity, nasal polyposis\nCentripetal obesity, cyanosis\nChronic productive cough, cyanosis\nCyanosis, heart murmurs\nHigh number of pack-years\nAssessed by number of “heads” or by daily duration',
    'Measurement of O₂ saturation\nClinical assessment\nClinical assessment\nClinical and radiologic assessment\nClinical and cardiologic assessment\nStandard clinical history taking\nDirected history taking\nDirected history taking',
    'None necessary\nWeight loss, CPAP during sleep\nWeight loss\nPulmonary management as indicated\nCorrective interventions as indicated\nInterventions to support cessation\nInterventions to support cessation\nAbstinence'],
  ['Secondary polycythemia',
    'Drugs\n  Erythropoietin\n  SGLT2 inhibitors\n  Androgen use\nPolycystic kidney disease\nTumors\n  Uterine myoma\n  Hepatoma\n  Medulloblastoma\n  Hypernephroma',
    'No longer frequently used in competitive sports\nUseful to correlate onset of polycythemia with onset of use\nInduce EPO gene expression\nTypical radiologic features\nTypical radiologic features',
    'Standard clinical history taking\nDirected history taking, including nonprescription use\nStandard clinical history, physical examination, and imaging studies\nStandard clinical history, physical examination, and imaging studies',
    'No long-term data available to inform management. Risk-benefit assessment probably favors continued use\nConsider phlebotomy to maintain hematocrit at 50%-52% prior to administration\nManaged according to clinical indications\nManaged according to clinical indications'],
  ['Congenital erythrocytosis',
    'EPOR mutations\nHIF1 mutations\nVHL mutations\nEGLN1 mutations',
    'Family history informative\nErythroid next-generation sequencing panels or whole-exome sequencing',
    'NA',
    'Expert opinion suggests maintaining hematocrit at approximately 52%'],
  ['Relative polycythemia',
    'Chronic decreased fluid intake\n  SGLT2 inhibitors',
    'Associated with a clinical phenotype of middle-aged, overweight men, often with “type A” personality and excess caffeine ingestion\nDiuretic effect',
    'Clinical assessment\nRed blood cell mass measurement may be helpful if available',
    'Encourage adequate fluid intake\nLifestyle modifications\nEncourage adequate fluid intake'],
]
const overview = computed(() => step.value === 0 || printing.value)
const views = [
  { band:0, columns:[1,2] }, { band:0, columns:[3,4] },
  { band:1, columns:[1,2] }, { band:1, columns:[3,4] },
  { band:2, columns:[1,2,3,4] }, { band:3, columns:[1,2,3,4] },
]
const view = computed(() => views[Math.max(0,step.value-1)])
const band = computed(() => bands[view.value.band])
</script>
<template>
  <div class="differential" :class="{ overview }" :data-reading-view="overview ? 0 : step">
    <table v-if="overview" aria-label="Differential Diagnosis of Polycythemia: complete overview">
      <colgroup><col style="width:14%"><col style="width:21%"><col style="width:23%"><col style="width:23%"><col style="width:19%"></colgroup>
      <thead><tr><th v-for="h in headers" :key="h" scope="col">{{h}}</th></tr></thead>
      <tbody><tr v-for="(row,i) in bands" :key="i"><td v-for="(cell,j) in row" :key="j" :class="{label:j===0}"><div v-for="(line,k) in cell.split('\n')" :key="k" :class="{indent:line.startsWith('  ')}">{{line.trim()}}</div></td></tr></tbody>
    </table>
    <div v-else :key="step" class="reading-view focus-enter" :class="{'four-columns':view.columns.length===4}">
      <div class="reading-heading"><h2>{{band[0]}}</h2><span>{{String(step).padStart(2,'0')}} / 06</span></div>
      <table :aria-label="`${band[0]}: enlarged reading view ${step}`">
        <thead><tr><th v-for="column in view.columns" :key="column" scope="col">{{headers[column]}}</th></tr></thead>
        <tbody><tr><td v-for="column in view.columns" :key="column"><div v-for="(line,k) in band[column].split('\n')" :key="k" :class="{indent:line.startsWith('  ')}">{{line.trim()}}</div></td></tr></tbody>
      </table>
    </div>
    <p class="abbreviations">CPAP, continuous positive airway pressure; OSA, obstructive sleep apnea; SGLT2, sodium-glucose cotransporter 2.</p>
  </div>
</template>
<style scoped>
.differential{font-variant-numeric:tabular-nums}.differential table{table-layout:fixed;font-size:26px;line-height:1.17;background:transparent!important}
.differential th{font-size:23px;padding:12px 20px;font-weight:600}.differential td{padding:16px 20px 14px}.differential td>div{margin-bottom:7px}.differential td>div:last-child{margin-bottom:0}
.differential .label{color:var(--wine);font-weight:650}.differential .indent{padding-left:18px}
.reading-heading{display:flex;justify-content:space-between;align-items:baseline;gap:30px;margin:0 0 16px}.reading-heading h2{font-size:30px!important;margin:0!important}.reading-heading>span{font-size:17px;letter-spacing:.1em;color:var(--muted)}
.four-columns th{font-size:21px;padding:12px 14px}.four-columns td{padding:18px 14px}.four-columns table{font-size:26px}
.abbreviations{font-size:16px!important;margin:12px 0 0!important;line-height:1.2!important;color:var(--muted)}
.overview table{font-size:12.5px;line-height:1.1}.overview th{font-size:14px;padding:6px 9px}.overview td{padding:6px 9px}.overview td>div{margin-bottom:2px}.overview .indent{padding-left:10px}.overview .abbreviations{font-size:14px!important;margin-top:8px!important}
</style>

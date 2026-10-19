<script setup lang="ts">
import { useFigureStep } from '../composables/useFigureStep'
const { step } = useFigureStep(3)
</script>
<template>
  <div class="criteria-atlas" :data-focus-step="step">
    <section class="criteria-region major-region" :class="{active:step===1}">
      <h2>Major criteria</h2>
      <ol>
        <li>Hemoglobin &gt;16.5 g/dL in men or &gt;16.0 g/dL in women or hematocrit &gt;49% in men or &gt;48% in women or red blood cell mass &gt;25% above mean normal predicted value</li>
        <li>Bone marrow biopsy showing age-adjusted hypercellularity with trilineage proliferation (panmyelosis), including prominent erythroid, granulocytic, and increase in pleomorphic, mature megakaryocytes without atypia</li>
        <li>Presence of <i>JAK2</i> V617F or <i>JAK2</i> exon 12 mutation</li>
      </ol>
    </section>
    <section class="criteria-region minor-region" :class="{active:step===2}">
      <h2>Minor criterion</h2>
      <p><span class="criterion-number">1.</span> Subnormal serum erythropoietin level</p>
    </section>
    <div class="criteria-qualifications" :class="{active:step===3}">
      <p>a All 3 major criteria or the first 2 of the major criteria together with the minor criterion are required for formal diagnosis.</p>
      <p>b SI conversion factors: To convert hemoglobin value to g/L, multiply by 10.0.</p>
    </div>
  </div>
</template>
<style scoped>
.criteria-atlas{display:grid;grid-template-columns:minmax(0,1fr) 268px;gap:24px 36px;font-variant-numeric:tabular-nums}
.criteria-region{padding:14px 0 6px 20px;border-top:2px solid var(--figure-line);border-left:3px solid transparent;transition:background 300ms,border-color 300ms}
.criteria-region.active{border-top-color:var(--wine);border-left-color:var(--wine);background:#f0e8ed}
.criteria-atlas h2{font-size:27px!important;margin:0 0 18px!important}.criteria-atlas ol{padding:0 12px 0 23px!important;margin:0!important}
.criteria-atlas li{font-size:25px;line-height:1.24;padding-left:6px;margin:0 0 19px!important}.criteria-atlas li:last-child{margin-bottom:0!important}
.minor-region{padding-right:12px}.minor-region p{font-size:28px;line-height:1.3;margin:0!important}.criterion-number{color:var(--wine)}
.criteria-qualifications{grid-column:1/-1;padding:14px 18px 2px;border-top:1px solid var(--rule);border-left:3px solid transparent;transition:background 300ms,border-color 300ms}
.criteria-qualifications.active{background:#eee7ed;border-left-color:var(--violet);border-top-color:var(--violet)}
.criteria-qualifications p{font-size:19px;line-height:1.26;margin:0 0 8px!important}
</style>

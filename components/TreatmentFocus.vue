<script setup lang="ts">
import { useFigureStep } from '../composables/useFigureStep'
const { step } = useFigureStep(2)
</script>
<template>
  <div class="treatment-focus" :data-focus-step="step">
    <section class="treatment-baseline" :class="{active:step===0}">
      <div><h2>For every patient</h2><p>Phlebotomy to Hct &lt;45%; low-dose aspirin when safe; control blood pressure, diabetes, lipids and smoking.</p></div>
      <div class="hematocrit-target"><span>Hct</span><strong>&lt;45<span>%</span></strong><img src="/art/atlas/erythrocyte.svg" alt="" aria-hidden="true" /></div>
    </section>
    <div class="conditional-treatments" :class="{active:step===1}">
      <section><h2>If high risk</h2><p>Age ≥60 or prior thrombosis → add cytoreduction.</p></section>
      <section><h2>If symptoms or poor control</h2><p>Consider cytoreduction for repeated phlebotomy, leukocytosis, splenomegaly or persistent symptom burden.</p></section>
    </div>
    <section class="treatment-strategies" :class="{active:step===2}"><h2>Available strategies</h2><p>Hydroxyurea, interferon or ruxolitinib according to age, tolerance and treatment goal; rusfertide is a 2026 targeted option for PV erythrocytosis.</p></section>
  </div>
</template>
<style scoped>
.treatment-focus{font-variant-numeric:tabular-nums;margin-top:12px}.treatment-focus h2{font-size:28px!important;margin:0 0 12px!important}.treatment-focus p{font-size:26px;line-height:1.29;margin:0!important}
.treatment-baseline{display:grid;grid-template-columns:1fr 235px;gap:44px;padding:22px 26px;border-left:3px solid var(--figure-line);background:#f1edf0;transition:background 300ms,border-color 300ms}
.treatment-baseline.active{background:#ebe1e8;border-color:var(--wine)}.hematocrit-target{align-self:center;justify-self:center}.hematocrit-target>span{display:block;color:var(--muted);font-size:20px}.hematocrit-target strong{font-size:77px;line-height:1;letter-spacing:-.045em;color:var(--wine)}.hematocrit-target strong span{font-size:47px}
.conditional-treatments{display:grid;grid-template-columns:1fr 1fr;gap:48px;margin:26px 0}
.conditional-treatments>section,.treatment-strategies{border-left:3px solid var(--figure-line);padding:12px 18px;transition:background 300ms,border-color 300ms}
.conditional-treatments.active>section,.treatment-strategies.active{background:#f0e8ed;border-color:var(--wine)}
.treatment-strategies{border-top:1px solid var(--rule)}.treatment-strategies p{font-size:24px}
.hematocrit-target{position:relative}.hematocrit-target img{position:absolute;right:-30px;top:0;width:50px;height:34px;object-fit:contain}
</style>

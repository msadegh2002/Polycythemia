<script setup lang="ts">
import {computed} from 'vue'
import {useFigureStep} from '../composables/useFigureStep'
const {step}=useFigureStep(3)
const branches=[
 {name:'Relative / apparent',title:'Reduced plasma volume',text:'Plasma volume is reduced; red-cell mass may be normal.',detail:'Dehydration • diuretics • stress erythrocytosis',x:50,y:200},
 {name:'Primary',title:'Intrinsic erythroid / marrow signaling defect',text:'EPOR mutation • Usually low EPO • Primary familial erythrocytosis',detail:'Acquired clonal PV: JAK2 V617F / exon 12. WHO-HAEM5: chronic myeloproliferative neoplasm.',x:280,y:300},
 {name:'Secondary',title:'External stimulus',text:'Hypoxia, EPO, drug or an EPO-producing lesion.',detail:'Congenital / hereditary: VHL • EGLN1 • EPAS1; high-affinity hemoglobin. Acquired: OSA • COPD • smoking / CO; renal / hepatic tumors; testosterone • EPO • SGLT2i.',x:490,y:300},
 {name:'Idiopathic',title:'No cause found',text:'No cause found after adequate evaluation.',detail:'',x:700,y:300},
]
const active=computed(()=>branches[step.value])
</script>
<template>
  <div class="classification-walkthrough">
    <svg viewBox="0 0 600 440" role="img" aria-label="Relative versus absolute erythrocytosis, then primary, secondary, and idiopathic branches">
      <text x="300" y="42" text-anchor="middle" class="root-label">ERYTHROCYTOSIS</text>
      <FigureConnector d="M300 62V114H104V169" :arrow="false" />
      <FigureConnector d="M300 62V114H382V173" :arrow="false" />
      <text x="382" y="202" text-anchor="middle" class="absolute-label">Absolute / true</text>
      <FigureConnector d="M382 218V283H154V332" :arrow="false" />
      <FigureConnector d="M382 218V283H337V332" :arrow="false" />
      <FigureConnector d="M382 218V283H520V332" :arrow="false" />
      <g class="branch" :class="{focused:step===0}"><rect x="19" y="169" width="170" height="81" rx="2"/><text x="104" y="200" text-anchor="middle" class="branch-label"><tspan x="104">Relative /</tspan><tspan x="104" dy="29">apparent</tspan></text></g>
      <g v-for="(label,i) in ['Primary','Secondary','Idiopathic']" :key="label" class="branch" :class="{focused:step===i+1}"><rect :x="69+i*183" y="332" width="170" height="66" rx="2"/><text :x="154+i*183" y="373" text-anchor="middle" class="branch-label">{{label}}</text></g>
      <FigureConnector :key="step" :d="step===0?'M300 62V114H104V169':`M300 62V114H382V173M382 218V283H${154+(step-1)*183}V332`" active :arrow="false" />
    </svg>
    <div class="branch-detail">
      <span class="detail-count">0{{step+1}} / 04</span><div :key="step" class="focus-enter"><h2>{{active.name}}</h2><p class="branch-mechanism">{{active.title}}</p><p>{{active.text}}</p><p class="detail-small">{{active.detail}}</p><p v-if="step===2" class="detail-small">Often normal / high EPO</p></div>
    </div>
  </div>
</template>
<style scoped>
.classification-walkthrough{display:grid;grid-template-columns:600px 1fr;gap:36px;align-items:center;margin-top:12px}.classification-walkthrough svg{width:600px;height:440px;overflow:visible}.root-label{font-size:29px;fill:var(--wine);font-weight:650}.absolute-label{font-size:28px;fill:var(--ink);font-weight:600}.branch-label{font-size:26px;fill:var(--ink);font-weight:550}.branch rect{fill:#f0ecf0;stroke:transparent;stroke-width:1;transition:fill 280ms,stroke 280ms}.branch.focused rect{fill:#e9dce5;stroke:#b995aa}.branch.focused .branch-label{fill:var(--wine);font-weight:650}.branch-detail{border-left:1px solid var(--rule);padding-left:30px;min-height:370px;padding-top:5px}.detail-count{font-size:17px;letter-spacing:.12em;color:var(--violet);display:block;margin-bottom:20px}.branch-detail h2{font-size:38px!important;line-height:1.12!important;margin-bottom:18px!important}.branch-detail p{font-size:27px;line-height:1.3;margin-bottom:18px!important}.branch-detail .branch-mechanism{font-size:25px;font-weight:600;color:var(--violet)}.branch-detail .detail-small{font-size:23px;color:var(--muted)}
@media(prefers-reduced-motion:reduce){*{transition:none!important}.branch-detail{opacity:1!important;transform:none!important}}
</style>

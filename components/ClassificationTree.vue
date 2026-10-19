<template>
  <div class="class-tree">
    <div class="root"><b>ERYTHROCYTOSIS / POLYCYTHEMIA</b><span>Raised hemoglobin or hematocrit — now identify the mechanism</span></div>
    <div class="branches">
      <section class="relative"><h3>RELATIVE / APPARENT</h3><p>Plasma volume is reduced;<br>red-cell mass may be normal.</p><p>Dehydration • diuretics • stress erythrocytosis</p></section>
      <section class="absolute-branch"><h3>ABSOLUTE / TRUE ERYTHROCYTOSIS</h3><p>True increase in red-cell mass.<br>The three etiologic branches below are all absolute erythrocytosis.</p><div class="etiologies"><section><h3>PRIMARY</h3><p>Intrinsic erythroid / marrow signaling defect</p><div class="leaves"><section><h4>CONGENITAL / HEREDITARY</h4><p>EPOR mutation<br>Usually low EPO<br>Primary familial erythrocytosis</p></section><section><h4>ACQUIRED CLONAL PV</h4><p>POLYCYTHEMIA VERA<br>JAK2 V617F / exon 12<br>WHO-HAEM5: chronic myeloproliferative neoplasm</p></section></div></section><section><h3>SECONDARY</h3><p>External stimulus: hypoxia, EPO, drug or an EPO-producing lesion</p><div class="leaves"><section><h4>CONGENITAL / HEREDITARY</h4><p>VHL • EGLN1 • EPAS1<br>High-affinity hemoglobin<br>Often normal / high EPO</p></section><section><h4>ACQUIRED</h4><p>OSA • COPD • smoking / CO<br>Renal / hepatic tumors<br>Testosterone • EPO • SGLT2i</p></section></div></section><section class="idiopathic"><h3>IDIOPATHIC</h3><p>No cause found after adequate evaluation</p></section></div></section>
    </div>
    <p class="tree-foot">WHO-HAEM5 places polycythemia vera under chronic myeloid neoplasms → myeloproliferative neoplasms.<br>Relative, secondary, hereditary and idiopathic categories are clinical differential categories used in the erythrocytosis work-up.</p>
  </div>
</template>
<style scoped>
.class-tree { font-size:19px; line-height:1.18; }
.root { width:650px; margin:0 auto 18px; padding:9px 14px; background:var(--wine); color:white; text-align:center; position:relative; }
.root b { font-size:24px; }.root span { display:block; font-size:18px; margin-top:5px; }
.root:after { content:''; position:absolute; width:1px; height:23px; bottom:-23px; left:50%; background:#bca8aa; }
.branches { display:grid; grid-template-columns:200px minmax(0,1fr); gap:24px; border-top:1px solid #bca8aa; padding-top:11px; }
.branches h3 { font-size:21px; margin:0 0 7px; }.branches p { font-size:19px; line-height:1.22; margin:0 0 9px; }
.relative { border-left:3px solid var(--wine); padding:8px 15px; }
.absolute-branch > h3,.absolute-branch > p { text-align:center; }
.etiologies { display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr) 120px; gap:18px; margin-top:13px; }
.etiologies > section { min-width:0; border-top:2px solid var(--wine); padding-top:10px; }
.leaves { display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:15px; border-top:1px solid #bca8aa; margin-top:11px; padding-top:10px; }
.leaves h4 { font-size:16px; color:var(--wine); font-weight:650; line-height:1.1; margin:0 0 9px; }
.leaves p { font-size:17px; line-height:1.24; margin:0; }
.tree-foot { border-top:1px solid var(--rule); margin-top:13px !important; padding-top:10px; font-size:17px !important; line-height:1.25 !important; }
</style>

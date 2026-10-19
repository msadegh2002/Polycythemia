<script setup lang="ts">
withDefaults(defineProps<{mixed?:boolean}>(),{mixed:true})
</script>
<template>
  <svg viewBox="0 0 300 350" role="img" :aria-label="mixed?'Marrow schematic with erythroid, leukocyte, and platelet illustrations; no quantitative scale':'Marrow erythropoiesis schematic; no quantitative scale'">
    <path d="M79 20C40 7 19 39 44 70L48 279C21 313 48 343 83 329L217 329C254 343 278 309 253 279L256 70C283 38 254 7 219 20Z" fill="#e8ded1" stroke="#b8aa9b" stroke-width="2"/>
    <path d="M89 44C63 32 45 50 65 78L70 273C52 296 67 319 90 306L208 306C234 320 248 297 231 275L235 78C254 54 239 33 212 44Z" fill="#f0e7eb" stroke="#c7b5c3" stroke-width="2"/>
    <path d="M67 81L110 62L157 98L209 58M70 143L114 113L154 145L221 111M74 214L115 179L169 209L229 172M78 280L119 249L175 279L229 245" fill="none" stroke="#d5c4ba" stroke-width="10" stroke-linejoin="round"/>
    <image href="/art/atlas/erythrocyte.svg" x="84" y="68" width="74" height="51" />
    <image href="/art/atlas/erythrocyte-oblique.svg" x="160" y="116" width="55" height="66" />
    <image href="/art/atlas/erythrocyte.svg" x="86" y="209" width="80" height="60" />
    <image href="/art/atlas/erythrocyte-front.svg" x="164" y="248" width="55" height="65" />
    <template v-if="mixed"><image href="/art/atlas/neutrophil.svg" x="85" y="133" width="73" height="76" /><image href="/art/atlas/platelet.svg" x="183" y="205" width="31" height="32" /><image href="/art/atlas/platelet.svg" x="152" y="281" width="24" height="25" /></template>
    <template v-else><image href="/art/atlas/erythrocyte.svg" x="89" y="138" width="72" height="55" /><image href="/art/atlas/erythrocyte-front.svg" x="164" y="181" width="52" height="61" /></template>
  </svg>
</template>

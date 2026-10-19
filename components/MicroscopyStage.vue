<script setup lang="ts">
defineProps<{image:'60160'|'60161'|'60164';specimen:string;label:string}>()
const names={
 '60160':'Polycythemia vera (PV), polycythemic phase, peripheral blood',
 '60161':'Polycythemia vera (PV), polycythemic phase, core biopsy 1',
 '60164':'Polycythemia vera (PV), polycythemic phase, aspirate smear',
}
</script>
<template>
  <div class="microscopy-stage">
    <figure class="full-micrograph"><img :src="`/images/ash-${image}.jpg`" :alt="names[image]" width="1000" height="753" /></figure>
    <aside><span class="specimen-word">{{specimen}}</span><div class="specimen-rule"></div><p>Polycythemia vera</p><p class="phase">Polycythemic phase</p><span class="image-id">ASH IMAGE BANK · {{image}}</span><div class="stage-credit">This image was originally published in ASH Image Bank. Elizabeth L. Courville. <a :href="`https://imagebank.hematology.org/image/${image}`" target="_blank" rel="noopener">{{names[image]}}.</a> ASH Image Bank. 2015; image {{image}}. © the American Society of Hematology.</div></aside>
  </div>
</template>
<style scoped>
.microscopy-stage{display:grid;grid-template-columns:minmax(0,780px) 1fr;gap:50px;align-items:start;margin-top:2px}.full-micrograph{margin:0}.full-micrograph img{height:535px;width:100%;object-fit:contain;object-position:left top}.microscopy-stage aside{padding-top:15px}.specimen-word{font-size:38px;line-height:1.07;color:#f2dfd8;display:block;font-weight:600;max-width:290px}.specimen-rule{height:3px;background:#c96572;width:58px;margin:28px 0}.microscopy-stage aside p{font-size:27px;line-height:1.2;margin-bottom:12px}.microscopy-stage aside .phase{font-size:23px;color:#cdbbb9}.image-id{display:block;font-size:14px;letter-spacing:.1em;line-height:1.6;color:#c6a9ae;margin-top:62px}.stage-credit{font-size:14px;line-height:1.32;color:#c8b7b7;margin-top:14px}.stage-credit a{color:inherit;text-decoration:underline;border:0}
</style>

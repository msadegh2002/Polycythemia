<script setup lang="ts">
withDefaults(defineProps<{variant?:'cover'|'erythrocyte'|'stem'|'kidney'|'specimen'|'marrow'|'treatment'|'none';inline?:boolean}>(),{variant:'none',inline:false})
const art='/art/atlas/'
</script>
<template>
  <div v-if="variant!=='none'" class="hematology-art atlas-art" :class="[variant,{inline}]" aria-hidden="true">
    <template v-if="variant==='cover'">
      <div class="hero-orbit"></div>
      <div v-for="(file,i) in ['erythrocyte-oblique','erythrocyte','erythrocyte-front','erythrocyte','erythrocyte-oblique']" :key="i" class="hero-cell" :class="`cell-${i}`">
        <img :src="`${art}${file}.svg`" alt="" v-motion :initial="{opacity:0,x:24,y:12}" :enter="{opacity:1,x:0,y:0,transition:{duration:500,delay:i*40}}" />
      </div>
    </template>
    <template v-else-if="variant==='erythrocyte'">
      <img class="rbc-main" :src="art+'erythrocyte.svg'" alt="" /><img class="rbc-back" :src="art+'erythrocyte-oblique.svg'" alt="" /><span class="art-caption">ERYTHROCYTES</span>
    </template>
    <template v-else-if="variant==='stem'">
      <img class="stem-main" :src="art+'stem-cell.svg'" alt="" /><span class="art-caption">HEMATOPOIETIC STEM CELL</span>
    </template>
    <template v-else-if="variant==='kidney'">
      <img class="kidney-main" :src="art+'kidney.svg'" alt="" /><span class="art-caption">KIDNEY / TISSUE SIGNAL</span>
    </template>
    <template v-else-if="variant==='specimen'">
      <img v-for="i in 3" :key="i" :class="`specimen-${i}`" :src="art+'specimen.svg'" alt="" /><img class="specimen-cell" :src="art+'erythrocyte.svg'" alt="" /><span class="art-caption">BLOOD SPECIMEN · SCHEMATIC</span>
    </template>
    <template v-else-if="variant==='marrow'">
      <MarrowIllustration /><span class="art-caption">MARROW · SCHEMATIC</span>
    </template>
    <template v-else-if="variant==='treatment'">
      <span class="target-label">Hct</span><span class="target-value">&lt;45<span>%</span></span><img :src="art+'erythrocyte.svg'" alt="" />
    </template>
  </div>
</template>
<style scoped>
.atlas-art{position:absolute;right:64px;top:230px;width:310px;height:370px;z-index:0;pointer-events:none}
.atlas-art img{position:absolute;object-fit:contain}.art-caption{position:absolute;bottom:0;left:0;right:0;font-size:14px;letter-spacing:.1em;line-height:1.25;color:var(--muted);text-align:center}
.cover{top:0;right:0;width:540px;height:720px;overflow:hidden}.hero-orbit{position:absolute;inset:90px -150px 55px 45px;border:1px solid #bb879547;border-radius:50%;transform:rotate(-25deg)}
.hero-cell{position:absolute;filter:drop-shadow(8px 22px 16px #0a091523)}.hero-cell img{position:relative;width:100%;height:100%;object-fit:contain}.cell-0{width:235px;height:250px;left:42px;top:45px;transform:rotate(-24deg);opacity:.5}.cell-1{width:380px;height:260px;left:155px;top:185px;transform:rotate(-18deg)}.cell-2{width:200px;height:230px;left:55px;top:422px;transform:rotate(15deg);opacity:.85}.cell-3{width:260px;height:180px;left:350px;top:570px;transform:rotate(-28deg);opacity:.5}.cell-4{width:135px;height:150px;left:430px;top:30px;transform:rotate(22deg);opacity:.3}
.erythrocyte .rbc-main{width:295px;height:210px;right:-10px;top:120px;transform:rotate(-14deg)}.erythrocyte .rbc-back{width:180px;height:190px;left:10px;top:0;transform:rotate(20deg);opacity:.55}
.stem-main{width:285px;height:300px;left:15px;top:12px}.kidney-main{width:220px;height:340px;left:45px;top:0}
.specimen img{height:300px;width:56px;top:0}.specimen-1{left:60px;transform:rotate(-10deg);opacity:.6}.specimen-2{left:130px;top:-20px!important}.specimen-3{left:200px;transform:rotate(10deg);opacity:.6}.specimen .specimen-cell{width:145px;height:110px;left:110px;top:245px;transform:rotate(-14deg)}
.marrow :deep(svg){width:100%;height:345px}.inline{display:block;position:relative;top:auto;right:auto;margin:0 auto;height:400px;width:250px}.inline.specimen img{height:330px}.inline .specimen-1{left:30px}.inline .specimen-2{left:100px}.inline .specimen-3{left:170px}.inline.specimen .specimen-cell{height:100px;left:100px;top:280px}
.treatment{height:170px;width:245px;top:140px;right:85px}.target-label{font-size:20px;color:var(--muted);position:absolute;top:5px;left:0}.target-value{position:absolute;top:20px;left:0;font-size:88px;letter-spacing:-.06em;font-weight:600;color:var(--wine);line-height:1.2}.target-value span{font-size:48px}.treatment img{width:100px;height:80px;right:-10px;top:90px;opacity:.5;transform:rotate(-20deg)}
@media(prefers-reduced-motion:reduce){.hero-cell img{opacity:1!important;transform:none!important}}
</style>

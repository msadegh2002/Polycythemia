<script setup lang="ts">
import manifest from '../slide-manifest.json'
import {computed} from 'vue'
const props=defineProps<{number:number|string;section?:string;light?:boolean}>()
const total=manifest.length
const entry=computed(()=>manifest[Number(props.number)-1])
const chapters=[['foundations','Erythrocytosis'],['secondary','Secondary'],['hereditary','Hereditary'],['pv','Polycythemia vera'],['laboratory','Laboratory & morphology'],['management','Complications & treatment']]
const chapterIndex=computed(()=>chapters.findIndex(c=>c[0]===entry.value?.chapter))
</script>
<template>
  <footer class="clinical-footer" :class="{light}">
    <span class="chapter-label"><span class="chapter-dots" aria-hidden="true"><i v-for="(c,i) in chapters" :key="c[0]" :class="{active:i===chapterIndex,done:i<chapterIndex}"></i></span>{{chapters[chapterIndex]?.[1] || section}}</span>
    <a v-if="entry?.illustrationCredit" class="art-credit" href="https://smart.servier.com/how-to-cite-servier-medical-art/" target="_blank" rel="noopener">Illustrations: Servier Medical Art · CC BY 4.0</a>
    <span>{{String(number).padStart(2,'0')}} <span class="slash">/</span> {{total}}</span>
  </footer>
</template>
<style scoped>
.clinical-footer{position:absolute;left:64px;right:64px;bottom:23px;display:flex;align-items:center;justify-content:space-between;font-size:14px;line-height:1;color:#81737d;letter-spacing:.025em;z-index:4;border-top:1px solid #d8d0d7;padding-top:12px}
.slash{margin:0 7px;opacity:.5}.light{color:#cbbcc9;border-color:#c6b6c53b}.chapter-label{display:flex;align-items:center;gap:15px}.chapter-dots{display:flex;gap:4px}.chapter-dots i{height:3px;width:16px;background:#c9bec83b}.chapter-dots i.done{background:#b98896}.chapter-dots i.active{background:var(--wine);height:6px}.light .chapter-dots i.active{background:#efc5cb}.art-credit{font-size:13px;letter-spacing:0;color:inherit;text-decoration:none!important;border:0!important;position:absolute;left:50%;transform:translateX(-30%);white-space:nowrap}
</style>

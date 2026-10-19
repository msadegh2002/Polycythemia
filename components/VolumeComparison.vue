<script setup lang="ts">
withDefaults(defineProps<{ compact?: boolean }>(), { compact:false })
const columns = [
  { x:85, height:136, cells:51, title:'Normal', sub:'Red-cell mass / plasma volume' },
  { x:350, height:176, cells:91, title:'Absolute erythrocytosis', sub:'Increased red-cell mass' },
  { x:615, height:94, cells:51, title:'Relative erythrocytosis', sub:'Reduced plasma volume' },
]
</script>
<template>
  <svg class="volume-diagram" viewBox="0 0 880 280" role="img" aria-label="Comparison of normal blood, increased red-cell mass, and reduced plasma volume; schematic, not quantitative">
    <g v-for="c in columns" :key="c.title">
      <rect :x="c.x" :y="205-c.height" width="132" :height="c.height" rx="4" fill="#efe5df" stroke="#d6c6c0" stroke-width="2" />
      <rect :x="c.x" :y="205-c.cells" width="132" :height="c.cells" rx="3" fill="#862d32" />
      <line :x1="c.x-8" :x2="c.x+140" y1="205" y2="205" stroke="#bca9a3" />
      <text :x="c.x+66" y="240" text-anchor="middle" fill="#64232b" style="font-size:23px;font-weight:650">{{ c.title }}</text>
      <text :x="c.x+66" y="266" text-anchor="middle" fill="#616973" style="font-size:18px">{{ c.sub }}</text>
    </g>
    <text x="2" y="100" fill="#616973" style="font-size:17px">Plasma</text>
    <text x="2" y="189" fill="#862d32" style="font-size:17px">Red cells</text>
    <text x="860" y="24" text-anchor="end" fill="#88818a" style="font-size:13px">Schematic</text>
  </svg>
</template>
<style scoped>.volume-diagram { display:block; width:100%; height:230px; margin:15px auto 12px; font-family:'Source Sans 3',sans-serif; }</style>

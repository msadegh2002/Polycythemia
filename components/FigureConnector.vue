<script setup lang="ts">
import { useId } from 'vue'
withDefaults(defineProps<{ d: string; active?: boolean; arrow?: boolean; signal?: boolean }>(), { active: false, arrow: true, signal: false })
const markerId = `figure-arrow-${useId().replace(/[^a-z0-9-]/gi, '')}`
</script>
<template>
  <g class="figure-connector" :class="{ active }" aria-hidden="true">
    <defs><marker :id="markerId" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M1 1L7 4L1 7" /></marker></defs>
    <path class="connector-track" :d="d" :marker-end="arrow ? `url(#${markerId})` : undefined" />
    <path class="connector-trace" :d="d" pathLength="1" :marker-end="active && arrow ? `url(#${markerId})` : undefined" />
    <circle v-if="signal && active" class="signal-packet" r="4" :style="{ offsetPath: `path('${d}')` }" />
  </g>
</template>
<style scoped>
.figure-connector { color:var(--wine); }
path { fill:none; stroke-width:2; stroke-linecap:round; stroke-linejoin:round; }
marker path { stroke:var(--figure-line,#c8bdc8); stroke-width:1.6; }
.active marker path { stroke:currentColor; }
.connector-track { stroke:var(--figure-line,#c8bdc8); }
.connector-trace { stroke:currentColor; stroke-dasharray:1; stroke-dashoffset:1; transition:stroke-dashoffset var(--path-duration,600ms) var(--figure-ease,ease); }
.active .connector-trace { stroke-dashoffset:0; animation:trace-figure var(--path-duration,600ms) var(--figure-ease,ease) var(--trace-delay,0ms) backwards; }
.signal-packet { fill:currentColor; opacity:0; offset-distance:0%; animation:carry-signal var(--path-duration,650ms) ease-out var(--trace-delay,0ms) both; }
@keyframes trace-figure { from{stroke-dashoffset:1} to{stroke-dashoffset:0} }
@keyframes carry-signal { 0%{offset-distance:0%;opacity:0} 12%{opacity:1} 85%{opacity:1} 100%{offset-distance:100%;opacity:0} }
@media(prefers-reduced-motion:reduce) { .connector-trace{transition:none;animation:none} .signal-packet{display:none} }
</style>

<script setup lang="ts">
defineProps<{ image: '60160' | '60161' | '60162' | '60164'; title: string }>()
const titles = {
  '60160': 'Polycythemia vera (PV), polycythemic phase, peripheral blood',
  '60161': 'Polycythemia vera (PV), polycythemic phase, core biopsy 1',
  '60162': 'Polycythemia vera (PV), polycythemic phase, core biopsy 2',
  '60164': 'Polycythemia vera (PV), polycythemic phase, aspirate smear',
}
</script>
<template>
  <figure class="microscopy">
    <img :src="`/images/ash-${image}.jpg`" :alt="titles[image]" width="1000" height="753" />
    <figcaption>
      <b>{{ title }}</b>
      <div class="source-credit">This image was originally published in ASH Image Bank. Elizabeth L. Courville.
        <a :href="`https://imagebank.hematology.org/image/${image}`" target="_blank" rel="noopener">{{ titles[image] }}.</a>
        ASH Image Bank. 2015; image {{ image }}. © the American Society of Hematology.
      </div>
    </figcaption>
  </figure>
</template>

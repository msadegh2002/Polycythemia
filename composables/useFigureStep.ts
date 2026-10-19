import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

/** Derive every teaching state from Slidev, including direct links and reverse navigation. */
export function useFigureStep(lastStep: number) {
  const { $clicks, $renderContext } = useSlideContext()
  const printing = computed(() => $renderContext.value === 'print')
  const step = computed(() => printing.value ? lastStep : Math.max(0, Math.min(lastStep, $clicks.value)))
  return { step, printing }
}

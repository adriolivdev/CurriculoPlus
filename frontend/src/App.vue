<template>
  <main class="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
    <div class="w-full max-w-3xl p-6 bg-white shadow-md rounded-xl">
      <component :is="currentStepComponent" @next="nextStep" @voltar="previousStep" />
    </div>
    <Footer />
  </main>
</template>

<script setup>
import { ref, computed } from 'vue'
import Footer from './components/Footer.vue'

import Step1DadosPessoais from './components/Step1DadosPessoais.vue'
import Step2ObjetivoFormacao from './components/Step2ObjetivoFormacao.vue'
import Step3Experiencia from './components/Step3Experiencia.vue'
import Step4HabilidadesIdiomas from './components/Step4HabilidadesIdiomas.vue'
import Step5CursosDisponibilidade from './components/Step5CursosDisponibilidade.vue'
import Step6Preview from './components/Step6Preview.vue'

// 🧩 Lista dos componentes por ordem
const steps = [
  Step1DadosPessoais,
  Step2ObjetivoFormacao,
  Step3Experiencia,
  Step4HabilidadesIdiomas,
  Step5CursosDisponibilidade,
  Step6Preview
]

const currentStep = ref(0)

// 🔁 Pega o componente da etapa atual
const currentStepComponent = computed(() => steps[currentStep.value])

// 👉 Avançar etapa
const nextStep = () => {
  if (currentStep.value < steps.length - 1) currentStep.value++
}

// 👈 Voltar etapa
const previousStep = () => {
  if (currentStep.value > 0) currentStep.value--
}
</script>

<style>
body {
  font-family: 'Inter', sans-serif;
  margin: 0;
}
</style>
   
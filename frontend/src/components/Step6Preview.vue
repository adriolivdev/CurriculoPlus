<template>
  <div class="space-y-6 max-h-[80vh] overflow-y-auto">
    <h2 class="text-2xl font-semibold text-center text-teal-600">6. Visualização Final</h2>

    <div class="border rounded-md p-4 bg-white shadow-sm">
      <!-- ... todos os dados do preview continuam iguais ... -->
    </div>

    <!-- Botões -->
    <div class="flex justify-between items-center">
      <button @click="$emit('voltar')" class="text-gray-600">Voltar e Editar</button>

      <button
        @click="gerarPdf"
        :disabled="carregando"
        class="relative bg-green-600 hover:bg-green-700 text-white py-2 px-6 rounded-md font-semibold"
      >
        <span v-if="!carregando">Baixar PDF</span>
        <span v-else>
          <svg class="animate-spin h-5 w-5 inline-block mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
          </svg>
          Gerando PDF...
        </span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useCurriculoStore } from '../stores/curriculo'
const store = useCurriculoStore()

const carregando = ref(false)

const formacoesValidas = computed(() =>
  store.formacoes.filter(f => f.tipo)
)

const experienciasValidas = computed(() =>
  store.experiencias.filter(e => e.empresa && e.cargo && e.periodo)
)

const gerarPdf = async () => {
  carregando.value = true
  try {
    const response = await fetch('https://seu-backend.render.com/gerar-pdf', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(store.$state)
    })

    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'curriculo.pdf'
    a.click()
    window.URL.revokeObjectURL(url)
  } catch (error) {
    console.error('Erro ao gerar PDF:', error)
    alert('Erro ao gerar PDF. Verifique o backend.')
  } finally {
    carregando.value = false
  }
}
</script>

<style scoped>
.tag {
  @apply text-white px-3 py-1 rounded-full text-sm bg-teal-600;
}
</style>

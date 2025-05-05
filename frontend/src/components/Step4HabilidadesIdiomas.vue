<template>
  <form @submit.prevent="$emit('next')" class="space-y-6">
    <h2 class="text-2xl font-semibold text-center text-teal-600">4. Habilidades e Idiomas</h2>

    <!-- Habilidades -->
    <div>
      <label class="block font-medium mb-1">Habilidades</label>
      <input
        type="text"
        v-model="novaHabilidade"
        @keyup.enter.prevent="adicionarHabilidadeDigitada"
        placeholder="Digite uma habilidade e pressione Enter"
        class="input"
      />
      <div class="flex flex-wrap gap-2 mt-2">
        <button
          v-for="h in habilidadesSugestao"
          :key="h"
          @click.prevent="adicionarHabilidade(h)"
          class="bg-teal-100 text-teal-800 text-sm px-3 py-1 rounded hover:bg-teal-200"
        >
          {{ h }}
        </button>
      </div>
      <div class="mt-3 flex flex-wrap gap-2">
        <span
          v-for="(h, index) in curriculo.habilidades"
          :key="index"
          class="bg-teal-600 text-white px-3 py-1 rounded-full text-sm flex items-center gap-2"
        >
          {{ h }}
          <button @click.prevent="removerHabilidade(index)" class="text-white hover:text-red-200 font-bold">×</button>
        </span>
      </div>
    </div>

    <!-- Idiomas -->
    <div>
      <label class="block font-medium mb-1">Idiomas</label>
      <input
        type="text"
        v-model="novoIdioma"
        @keyup.enter.prevent="adicionarIdiomaDigitado"
        placeholder="Digite um idioma e pressione Enter"
        class="input"
      />
      <div class="flex flex-wrap gap-2 mt-2">
        <button
          v-for="i in idiomasSugestao"
          :key="i"
          @click.prevent="adicionarIdioma(i)"
          class="bg-blue-100 text-blue-800 text-sm px-3 py-1 rounded hover:bg-blue-200"
        >
          {{ i }}
        </button>
      </div>
      <div class="mt-3 flex flex-wrap gap-2">
        <span
          v-for="(i, index) in curriculo.idiomas"
          :key="index"
          class="bg-blue-600 text-white px-3 py-1 rounded-full text-sm flex items-center gap-2"
        >
          {{ i }}
          <button @click.prevent="removerIdioma(index)" class="text-white hover:text-red-200 font-bold">×</button>
        </span>
      </div>
    </div>

    <!-- Navegação -->
    <div class="flex justify-between">
      <button type="button" @click="$emit('voltar')" class="text-gray-600">Voltar</button>
      <button type="submit" class="bg-teal-600 hover:bg-teal-700 text-white py-2 px-6 rounded-md font-semibold">Próximo</button>
    </div>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useCurriculoStore } from '../stores/curriculo'
const curriculo = useCurriculoStore()

const novaHabilidade = ref('')
const novoIdioma = ref('')

const habilidadesSugestao = [
  'Comunicação', 'Organização', 'Proatividade', 'Excel', 'Liderança',
  'Raciocínio lógico', 'Trabalho em equipe', 'Adaptabilidade',
  'Resolução de problemas', 'Criatividade', 'Gestão de tempo', 'Empatia'
]

const idiomasSugestao = [
  'Português Nativo', 'Inglês Básico', 'Inglês Intermediário', 'Inglês Avançado',
  'Espanhol Básico', 'Francês Básico', 'Italiano Básico', 'Alemão Básico'
]

// Clique em botão sugestão
const adicionarHabilidade = (h) => {
  const valor = h.trim()
  if (valor && !curriculo.habilidades.includes(valor)) {
    curriculo.habilidades.push(valor)
  }
}

// Enter digitando
const adicionarHabilidadeDigitada = () => {
  const valor = novaHabilidade.value.trim()
  if (valor && !curriculo.habilidades.includes(valor)) {
    curriculo.habilidades.push(valor)
  }
  novaHabilidade.value = ''
}

const removerHabilidade = (index) => {
  curriculo.habilidades.splice(index, 1)
}

// Clique em botão sugestão
const adicionarIdioma = (i) => {
  const valor = i.trim()
  if (valor && !curriculo.idiomas.includes(valor)) {
    curriculo.idiomas.push(valor)
  }
}

// Enter digitando
const adicionarIdiomaDigitado = () => {
  const valor = novoIdioma.value.trim()
  if (valor && !curriculo.idiomas.includes(valor)) {
    curriculo.idiomas.push(valor)
  }
  novoIdioma.value = ''
}

const removerIdioma = (index) => {
  curriculo.idiomas.splice(index, 1)
}
</script>

<style scoped>
.input {
  @apply w-full border rounded-md px-4 py-2 mt-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500;
}
</style>

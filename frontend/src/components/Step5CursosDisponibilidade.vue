<template>
  <form @submit.prevent="$emit('next')" class="space-y-6">
    <h2 class="text-2xl font-semibold text-center text-teal-600">5. Cursos e Disponibilidade</h2>

    <!-- Cursos -->
    <div>
      <label class="block font-medium mb-1">Cursos Complementares</label>
      <input
        type="text"
        v-model="novoCurso"
        @keydown.enter.prevent="adicionarCursoManual"
        placeholder="Selecione ou Digite um idioma e pressione Enter"
        class="input"
      />
      <div class="flex flex-wrap gap-2 mt-2">
        <button
          v-for="curso in cursosSugestao"
          :key="curso"
          type="button"
          :class="{
            'bg-amber-500 text-white': curriculo.cursos.includes(curso),
            'bg-amber-100 text-amber-800 hover:bg-amber-200': !curriculo.cursos.includes(curso),
            'text-sm px-3 py-1 rounded': true
          }"
          @click="toggleCurso(curso)"
        >
          {{ curso }}
        </button>
      </div>
      <div class="mt-3 flex flex-wrap gap-2">
        <span
          v-for="(c, index) in curriculo.cursos"
          :key="index"
          class="bg-amber-500 text-white px-3 py-1 rounded-full text-sm flex items-center gap-2"
        >
          {{ c }}
          <button @click.prevent="removerCurso(index)" class="text-white hover:text-red-200 font-bold">×</button>
        </span>
      </div>
    </div>

    <!-- Disponibilidade -->
    <div>
      <label class="block font-medium mb-1">Disponibilidade</label>
      <input
        type="text"
        v-model="novaDisponibilidade"
        @keydown.enter.prevent="adicionarDisponibilidadeManual"
        placeholder="Selecione ou Digite um idioma e pressione Enter"
        class="input"
      />
      <div class="flex flex-wrap gap-2 mt-2">
        <button
          v-for="d in disponibilidadeSugestao"
          :key="d"
          type="button"
          :class="{
            'bg-indigo-600 text-white': curriculo.disponibilidades.includes(d),
            'bg-indigo-100 text-indigo-800 hover:bg-indigo-200': !curriculo.disponibilidades.includes(d),
            'text-sm px-3 py-1 rounded': true
          }"
          @click="toggleDisponibilidade(d)"
        >
          {{ d }}
        </button>
      </div>
      <div class="mt-3 flex flex-wrap gap-2">
        <span
          v-for="(d, index) in curriculo.disponibilidades"
          :key="index"
          class="bg-indigo-600 text-white px-3 py-1 rounded-full text-sm flex items-center gap-2"
        >
          {{ d }}
          <button @click.prevent="removerDisponibilidade(index)" class="text-white hover:text-red-200 font-bold">×</button>
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

const novoCurso = ref('')
const novaDisponibilidade = ref('')

const cursosSugestao = [
  'Informática Básica', 'Excel Avançado', 'Atendimento ao Cliente',
  'Técnicas de Vendas', 'Gestão de Tempo', 'Comunicação Empresarial'
]

const disponibilidadeSugestao = [
  'Integral', 'Manhã', 'Tarde', 'Noite', 'Fins de semana', 'Imediata', 'Sábados', 'Domingos'
]

// Cursos
const adicionarCursoManual = () => {
  const valor = novoCurso.value.trim()
  if (valor && !curriculo.cursos.includes(valor)) {
    curriculo.cursos.push(valor)
  }
  novoCurso.value = ''
}

const toggleCurso = (curso) => {
  const index = curriculo.cursos.indexOf(curso)
  if (index >= 0) {
    curriculo.cursos.splice(index, 1)
  } else {
    curriculo.cursos.push(curso)
  }
}

const removerCurso = (index) => {
  curriculo.cursos.splice(index, 1)
}

// Disponibilidade
const adicionarDisponibilidadeManual = () => {
  const valor = novaDisponibilidade.value.trim()
  if (valor && !curriculo.disponibilidades.includes(valor)) {
    curriculo.disponibilidades.push(valor)
  }
  novaDisponibilidade.value = ''
}

const toggleDisponibilidade = (d) => {
  const index = curriculo.disponibilidades.indexOf(d)
  if (index >= 0) {
    curriculo.disponibilidades.splice(index, 1)
  } else {
    curriculo.disponibilidades.push(d)
  }
}

const removerDisponibilidade = (index) => {
  curriculo.disponibilidades.splice(index, 1)
}
</script>

<style scoped>
.input {
  @apply w-full border rounded-md px-4 py-2 mt-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500;
}
</style>

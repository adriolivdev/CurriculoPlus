<template>
  <form @submit.prevent="$emit('next')" class="space-y-6" autocomplete="off">
    <h2 class="text-2xl font-semibold text-center text-teal-600">5. Cursos e Disponibilidade</h2>

    <!-- CURSOS -->
    <div>
      <label class="block font-medium mb-1">Cursos Complementares</label>
      <input
        ref="inputCurso"
        type="text"
        v-model="novoCurso"
        @keydown.enter.prevent.stop="adicionarCursoDigitado"
        placeholder="Digite um curso e pressione Enter"
        class="input"
        autocomplete="off"
      />
      <div class="flex flex-wrap gap-2 mt-2">
        <button
          type="button"
          v-for="curso in cursosSugestao"
          :key="curso"
          @click.prevent="adicionarCurso(curso)"
          class="bg-amber-100 text-amber-800 text-sm px-3 py-1 rounded hover:bg-amber-200"
        >
          {{ curso }}
        </button>
      </div>
      <div class="mt-2 flex flex-wrap gap-2">
        <span
          v-for="(c, index) in curriculo.cursos"
          :key="index"
          class="bg-amber-500 text-white px-3 py-1 rounded-full text-sm flex items-center gap-2"
        >
          {{ c }}
          <button type="button" @click.prevent="removerCurso(index)" class="text-white hover:text-red-200 font-bold">×</button>
        </span>
      </div>
    </div>

    <!-- DISPONIBILIDADE -->
    <div>
      <label class="block font-medium mb-1">Disponibilidade</label>
      <input
        ref="inputDisponibilidade"
        type="text"
        v-model="novaDisponibilidade"
        @keydown.enter.prevent.stop="adicionarDisponibilidadeDigitada"
        placeholder="Digite uma disponibilidade e pressione Enter"
        class="input"
        autocomplete="off"
      />
      <div class="flex flex-wrap gap-2 mt-2">
        <button
          type="button"
          v-for="d in disponibilidadeSugestao"
          :key="d"
          @click.prevent="adicionarDisponibilidade(d)"
          class="bg-indigo-100 text-indigo-800 text-sm px-3 py-1 rounded hover:bg-indigo-200"
        >
          {{ d }}
        </button>
      </div>
      <div class="mt-2 flex flex-wrap gap-2">
        <span
          v-for="(d, index) in curriculo.disponibilidades"
          :key="index"
          class="bg-indigo-600 text-white px-3 py-1 rounded-full text-sm flex items-center gap-2"
        >
          {{ d }}
          <button type="button" @click.prevent="removerDisponibilidade(index)" class="text-white hover:text-red-200 font-bold">×</button>
        </span>
      </div>
    </div>

    <!-- NAVEGAÇÃO -->
    <div class="flex justify-between">
      <button type="button" @click="$emit('voltar')" class="text-gray-600">Voltar</button>
      <button type="submit" class="bg-teal-600 hover:bg-teal-700 text-white py-2 px-6 rounded-md font-semibold">Próximo</button>
    </div>
  </form>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import { useCurriculoStore } from '../stores/curriculo'
const curriculo = useCurriculoStore()

const novoCurso = ref('')
const novaDisponibilidade = ref('')
const inputCurso = ref(null)
const inputDisponibilidade = ref(null)

const cursosSugestao = [
  'Informática Básica', 'Excel Avançado', 'Atendimento ao Cliente',
  'Técnicas de Vendas', 'Gestão de Tempo', 'Comunicação Empresarial'
]

const disponibilidadeSugestao = [
  'Integral', 'Manhã', 'Tarde', 'Noite', 'Fins de semana', 'Imediata', 'Sábados', 'Domingos'
]

// CURSO DIGITADO
const adicionarCursoDigitado = () => {
  const valor = novoCurso.value.trim()
  if (valor && !curriculo.cursos.includes(valor)) {
    curriculo.cursos.push(valor)
  }
  novoCurso.value = ''
  nextTick(() => inputCurso.value?.focus())
}

// CURSO SUGERIDO
const adicionarCurso = (curso) => {
  if (!curso || typeof curso !== 'string') return
  const valor = curso.trim()
  if (valor && !curriculo.cursos.includes(valor)) {
    curriculo.cursos.push(valor)
  }
}

const removerCurso = (index) => {
  curriculo.cursos.splice(index, 1)
}

// DISPONIBILIDADE
const adicionarDisponibilidadeDigitada = () => {
  const valor = novaDisponibilidade.value.trim()
  if (valor && !curriculo.disponibilidades.includes(valor)) {
    curriculo.disponibilidades.push(valor)
  }
  novaDisponibilidade.value = ''
  nextTick(() => inputDisponibilidade.value?.focus())
}

const adicionarDisponibilidade = (d) => {
  if (!d || typeof d !== 'string') return
  const valor = d.trim()
  if (valor && !curriculo.disponibilidades.includes(valor)) {
    curriculo.disponibilidades.push(valor)
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

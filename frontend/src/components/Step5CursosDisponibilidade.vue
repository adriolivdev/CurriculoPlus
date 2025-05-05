<template>
  <form @submit.prevent="$emit('next')" class="space-y-6">
    <h2 class="text-2xl font-semibold text-center text-teal-600">5. Cursos e Disponibilidade</h2>

    <!-- Cursos Complementares -->
    <div>
      <label class="block font-medium mb-1">Cursos Complementares</label>
      <input
        type="text"
        v-model="novoCurso"
        @keydown.enter.prevent="confirmarCursoDigitado"
        placeholder="Digite um curso e pressione Enter"
        class="input"
      />
      <div class="flex gap-2 mt-2 overflow-x-auto pb-1">
        <button
          v-for="curso in cursosSugestao"
          :key="curso"
          type="button"
          @click="adicionarCurso(curso)"
          class="min-w-max bg-amber-100 text-amber-800 text-sm px-3 py-1 rounded hover:bg-amber-200"
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
        @keydown.enter.prevent="confirmarDisponibilidadeDigitada"
        placeholder="Digite uma disponibilidade e pressione Enter"
        class="input"
      />
      <div class="flex gap-2 mt-2 overflow-x-auto pb-1">
        <button
          v-for="d in disponibilidadeSugestao"
          :key="d"
          type="button"
          @click="adicionarDisponibilidade(d)"
          class="min-w-max bg-indigo-100 text-indigo-800 text-sm px-3 py-1 rounded hover:bg-indigo-200"
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

const adicionarCurso = (c) => {
  const valor = c.trim()
  if (valor && !curriculo.cursos.includes(valor)) {
    curriculo.cursos.push(valor)
  }
}

const confirmarCursoDigitado = () => {
  const valor = novoCurso.value.trim()
  if (valor && !curriculo.cursos.includes(valor)) {
    curriculo.cursos.push(valor)
  }
  novoCurso.value = ''
}

const removerCurso = (index) => {
  curriculo.cursos.splice(index, 1)
}

const adicionarDisponibilidade = (d) => {
  const valor = d.trim()
  if (valor && !curriculo.disponibilidades.includes(valor)) {
    curriculo.disponibilidades.push(valor)
  }
}

const confirmarDisponibilidadeDigitada = () => {
  const valor = novaDisponibilidade.value.trim()
  if (valor && !curriculo.disponibilidades.includes(valor)) {
    curriculo.disponibilidades.push(valor)
  }
  novaDisponibilidade.value = ''
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

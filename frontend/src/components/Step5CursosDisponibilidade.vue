<template>
    <form @submit.prevent="$emit('next')" class="space-y-6">
      <h2 class="text-2xl font-semibold text-center text-teal-600">5. Cursos e Disponibilidade</h2>
  
      <!-- Cursos Complementares -->
      <div>
        <label class="block font-medium mb-1">Cursos Complementares</label>
        <input
          type="text"
          v-model="novoCurso"
          @keyup.enter="adicionarCurso"
          placeholder="Digite um curso e pressione Enter"
          class="input"
        />
        <div class="flex flex-wrap gap-2 mt-2">
          <button
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
            class="bg-amber-500 text-white px-3 py-1 rounded-full text-sm"
          >
            {{ c }}
          </span>
        </div>
      </div>
  
      <!-- Disponibilidade -->
      <div>
        <label class="block font-medium mb-1">Disponibilidade</label>
        <input
          type="text"
          v-model="novaDisponibilidade"
          @keyup.enter="adicionarDisponibilidade"
          placeholder="Digite uma disponibilidade e pressione Enter"
          class="input"
        />
        <div class="flex flex-wrap gap-2 mt-2">
          <button
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
            class="bg-indigo-600 text-white px-3 py-1 rounded-full text-sm"
          >
            {{ d }}
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
  
  const adicionarCurso = (curso = novoCurso.value) => {
    if (curso && !curriculo.cursos.includes(curso)) curriculo.cursos.push(curso)
    novoCurso.value = ''
  }
  
  const adicionarDisponibilidade = (d = novaDisponibilidade.value) => {
    if (d && !curriculo.disponibilidades.includes(d)) curriculo.disponibilidades.push(d)
    novaDisponibilidade.value = ''
  }
  </script>
  
  <style scoped>
  .input {
    @apply w-full border rounded-md px-4 py-2 mt-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500;
  }
  </style>
  
<template>
    <form @submit.prevent="$emit('next')" class="space-y-4">
      <h2 class="text-2xl font-semibold text-center text-teal-600">3. Experiência Profissional</h2>
  
      <div>
        <label class="block font-medium">Situação atual</label>
        <select v-model="curriculo.statusExperiencia" class="input" @change="limparExperienciasSeNecessario">
          <option disabled value="">Selecione</option>
          <option>Em busca do primeiro emprego</option>
          <option>Tenho experiências anteriores</option>
        </select>
      </div>
  
      <div v-if="curriculo.statusExperiencia === 'Tenho experiências anteriores'" class="space-y-6">
        <div v-for="(exp, index) in curriculo.experiencias" :key="index" class="border-t pt-4">
          <h3 class="font-semibold text-lg text-teal-700">Experiência {{ index + 1 }}</h3>
  
          <div>
            <label class="block font-medium">Empresa</label>
            <input type="text" v-model="exp.empresa" class="input" placeholder="Ex: Nome da empresa" />
          </div>
  
          <div>
            <label class="block font-medium">Cargo</label>
            <input type="text" v-model="exp.cargo" class="input" placeholder="Ex: Auxiliar Administrativo" />
          </div>
  
          <div>
            <label class="block font-medium">Período</label>
            <input type="text" v-model="exp.periodo" class="input" placeholder="Ex: 2020 - 2022" />
          </div>
  
          <div>
            <label class="block font-medium">Atividades</label>
            <textarea v-model="exp.atividades" rows="2" class="input" placeholder="Principais responsabilidades e atividades..."></textarea>
          </div>
        </div>
      </div>
  
      <div class="flex justify-between">
        <button type="button" @click="$emit('voltar')" class="text-gray-600">Voltar</button>
        <button type="submit" class="bg-teal-600 hover:bg-teal-700 text-white py-2 px-6 rounded-md font-semibold">Próximo</button>
      </div>
    </form>
  </template>
  
  <script setup>
  import { useCurriculoStore } from '../stores/curriculo'
  const curriculo = useCurriculoStore()
  
  const limparExperienciasSeNecessario = () => {
    if (curriculo.statusExperiencia !== 'Tenho experiências anteriores') {
      curriculo.experiencias = curriculo.experiencias.map(() => ({
        empresa: '', cargo: '', periodo: '', atividades: ''
      }))
    }
  }
  </script>
  
  <style scoped>
  .input {
    @apply w-full border rounded-md px-4 py-2 mt-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500;
  }
  </style>
  
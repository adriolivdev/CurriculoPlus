<template>
  <form @submit.prevent="$emit('next')" class="space-y-4">
    <h2 class="text-2xl font-semibold text-center text-teal-600">2. Objetivo e Formação</h2>

    <!-- Nível / Cargo pretendido -->
    <div>
      <label class="block font-medium">Nível / Cargo pretendido</label>
      <select v-model="nivel" class="input">
        <option disabled value="">Selecione</option>
        <option>Aprendiz</option>
        <option>Estagiário</option>
        <option>Júnior</option>
        <option>Pleno</option>
        <option>Sênior</option>
        <option>Outro</option>
      </select>
    </div>

    <!-- Área de atuação -->
    <div>
      <label class="block font-medium">Área de atuação</label>
      <select v-model="area" class="input">
        <option disabled value="">Selecione</option>
        <option>Administração</option>
        <option>TI</option>
        <option>Atendimento</option>
        <option>Serviços Gerais</option>
        <option>Financeiro</option>
        <option>Marketing</option>
        <option>Outro</option>
      </select>
    </div>

    <!-- Objetivo profissional (preenchido automaticamente, mas editável) -->
    <div>
      <label class="block font-medium">Objetivo Profissional</label>
      <textarea
        v-model="objetivo"
        rows="3"
        class="input"
        placeholder="Seu objetivo será gerado automaticamente, mas pode ser editado."
      ></textarea>
    </div>

    <!-- Formação Acadêmica -->
    <div>
      <label class="block font-medium">Formação Acadêmica</label>
      <div v-for="(formacao, index) in formacoes" :key="index" class="mb-4 space-y-1 border-b pb-3">
        <select v-model="formacao.tipo" class="input">
          <option disabled value="">Tipo de Formação</option>
          <option>Curso Profissionalizante</option>
          <option>Ensino Fundamental Incompleto</option>
          <option>Ensino Fundamental Completo</option>
          <option>Ensino Médio Incompleto</option>
          <option>Ensino Médio Completo</option>
          <option>Técnico</option>
          <option>Graduação</option>
          <option>Pós-graduação</option>
          <option>Mestrado</option>
          <option>Doutorado</option>
        </select>

        <input type="text" v-model="formacao.nomeEscola" class="input" placeholder="Nome da escola" />
        <input type="text" v-model="formacao.nomeCurso" class="input" placeholder="Nome do curso (opcional)" />

        <div class="flex gap-2">
          <input type="text" v-model="formacao.inicio" class="input w-1/2" placeholder="Início (ex: 2020)" />
          <input type="text" v-model="formacao.fim" class="input w-1/2" placeholder="Término (ex: 2022)" />
        </div>

        <button type="button" @click="removerFormacao(index)" class="text-red-600 text-sm">Remover</button>
      </div>
      <button type="button" @click="adicionarFormacao" class="text-teal-600 font-medium">
        + Adicionar outra formação
      </button>
    </div>

    <!-- Navegação -->
    <div class="flex justify-between">
      <button type="button" @click="$emit('voltar')" class="text-gray-600">Voltar</button>
      <button type="submit" class="bg-teal-600 hover:bg-teal-700 text-white py-2 px-6 rounded-md font-semibold">
        Próximo
      </button>
    </div>
  </form>
</template>

<script setup>
import { computed, watch } from 'vue'
import { useCurriculoStore } from '../stores/curriculo'

const store = useCurriculoStore()

// Computed bindings direto do store
const nivel = computed({
  get: () => store.nivel,
  set: val => (store.nivel = val)
})
const area = computed({
  get: () => store.area,
  set: val => (store.area = val)
})
const objetivo = computed({
  get: () => store.objetivo,
  set: val => (store.objetivo = val)
})
const formacoes = computed({
  get: () => store.formacoes,
  set: val => (store.formacoes = val)
})

// 🎯 Função que retorna o objetivo personalizado
const gerarObjetivo = (nivel, area) => {
  if (!nivel || !area || nivel === 'Outro' || area === 'Outro') {
    return 'Busco uma oportunidade profissional para desenvolver minhas habilidades e contribuir com a equipe.'
  }
  const base = {
    Aprendiz: `Busco minha primeira oportunidade como aprendiz na área de ${area}, onde possa aprender e crescer profissionalmente.`,
    Estagiário: `Procuro uma vaga de estágio em ${area} para aplicar meus conhecimentos acadêmicos e adquirir experiência prática.`,
    Júnior: `Atuar como profissional júnior em ${area}, contribuindo com energia e vontade de aprender em um ambiente desafiador.`,
    Pleno: `Contribuir com minha experiência e habilidades na área de ${area}, atuando como profissional pleno e ajudando no desenvolvimento da equipe.`,
    Sênior: `Atuar como profissional sênior em ${area}, oferecendo liderança técnica, visão estratégica e colaboração ativa nos resultados da empresa.`,
    Outro: `Busco uma oportunidade profissional na área de ${area}.`
  }
  return base[nivel] || base["Outro"]
}

// ⚡️ Atualiza objetivo automaticamente ao mudar nível ou área
watch([nivel, area], () => {
  objetivo.value = gerarObjetivo(nivel.value, area.value)
})

// 🏫 Adicionar / remover formação
const adicionarFormacao = () => {
  formacoes.value.push({ tipo: '', nomeEscola: '', nomeCurso: '', inicio: '', fim: '' })
}
const removerFormacao = index => {
  formacoes.value.splice(index, 1)
}
</script>

<style scoped>
.input {
  @apply w-full border rounded-md px-4 py-2 mt-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500;
}
</style>

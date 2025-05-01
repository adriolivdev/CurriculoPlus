<template>
  <form @submit.prevent="$emit('next')" class="space-y-4">
    <h2 class="text-2xl font-semibold text-center text-teal-600">1. Dados Pessoais</h2>

    <!-- Nome -->
    <div>
      <label class="block font-medium">Nome completo</label>
      <input type="text" v-model="nome" class="input" placeholder="Ex: Adriane Oliveira" required />
    </div>

    <!-- Email -->
    <div>
      <label class="block font-medium">Email</label>
      <input type="email" v-model="email" class="input" placeholder="Ex: voce@email.com" required />
    </div>

    <!-- Idade -->
    <div>
      <label class="block font-medium">Idade</label>
      <input type="number" v-model="idade" class="input" placeholder="Ex: 25" />
    </div>

    <!-- Estado civil -->
    <div>
      <label class="block font-medium">Estado civil</label>
      <select v-model="estadoCivil" class="input">
        <option disabled value="">Selecione</option>
        <option>Solteiro(a)</option>
        <option>Casado(a)</option>
        <option>Divorciado(a)</option>
        <option>Viúvo(a)</option>
      </select>
    </div>

    <!-- Foto -->
    <div>
      <label class="block font-medium">Foto (opcional)</label>
      <input type="file" accept="image/*" @change="handleFoto" class="input" />
      <div v-if="foto" class="mt-2 flex justify-center">
        <img :src="foto" alt="Prévia da foto" class="w-24 h-24 rounded-full object-cover border" />
      </div>
    </div>

    <div class="flex justify-end">
      <button type="submit" class="bg-teal-600 hover:bg-teal-700 text-white py-2 px-6 rounded-md font-semibold">
        Próximo
      </button>
    </div>
  </form>
</template>

<script setup>
import { computed } from 'vue'
import { useCurriculoStore } from '../stores/curriculo'

const store = useCurriculoStore()

const nome = computed({
  get: () => store.nome,
  set: val => (store.nome = val)
})
const email = computed({
  get: () => store.email,
  set: val => (store.email = val)
})
const idade = computed({
  get: () => store.idade,
  set: val => (store.idade = val)
})
const estadoCivil = computed({
  get: () => store.estadoCivil,
  set: val => (store.estadoCivil = val)
})
const foto = computed({
  get: () => store.foto,
  set: val => (store.foto = val)
})

// Converte a imagem para base64
const handleFoto = (e) => {
  const file = e.target.files[0]
  if (!file) return

  const reader = new FileReader()
  reader.onload = () => {
    foto.value = reader.result
  }
  reader.readAsDataURL(file)
}
</script>

<style scoped>
.input {
  @apply w-full border rounded-md px-4 py-2 mt-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500;
}
</style>

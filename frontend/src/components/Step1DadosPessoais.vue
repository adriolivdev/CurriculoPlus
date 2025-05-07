<template>
  <form @submit.prevent="$emit('next')" class="space-y-4">
    <!-- Cabeçalho e explicação -->
    <div class="text-center space-y-2 mb-4">
      <h2 class="text-2xl font-bold text-teal-600">🚀 Gerador de Currículos Inteligente</h2>
      <p class="text-gray-700 text-sm">
        Preencha seus dados passo a passo. Ao final, você poderá <strong>visualizar, revisar e baixar</strong> seu currículo em PDF com um clique!
      </p>
      <p class="text-gray-600 text-xs italic">Etapa 1 de 6: Informações pessoais</p>
    </div>

    <!-- Nome -->
    <div>
      <label class="block font-medium">Nome completo</label>
      <input type="text" v-model="nome" class="input" placeholder="Ex: João da Silva Costa" required />
    </div>

    <!-- Email -->
    <div>
      <label class="block font-medium">Email</label>
      <input type="email" v-model="email" class="input" placeholder="Ex: seuemail@email.com" required />
    </div>

    <!--Endereço-->
    <div>
      <label class="block font-medium">Endereço</label>
      <input type="text" v-model="endereco" class="input" placeholder="Ex: Rua das Flores, 123" required />
    </div>

    <!-- Telefone -->
    <div>
      <label class="block font-medium">Telefone</label>
      <input type="tel" v-model="telefone" class="input" placeholder="Ex: (99) 99999-9999" required />
    </div>

    <!-- Idade -->
    <div>
      <label class="block font-medium">Idade</label>
      <input type="number" v-model="idade" class="input" placeholder="Ex: 25" required />
    </div>

    <!-- Estado civil -->
    <div>
      <label class="block font-medium">Estado civil</label>
      <select v-model="estadoCivil" class="input" required>
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

    <!-- Botão de próximo -->
    <div class="flex justify-end mt-4">
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

const endereco = computed({
  get: () => store.endereco,
  set: val => (store.endereco = val)
})
const telefone = computed({
  get: () => store.telefone,
  set: val => (store.telefone = val)
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

<template>
  <div class="space-y-6 max-h-[80vh] overflow-y-auto">
    <h2 class="text-2xl font-semibold text-center text-teal-600">6. Visualização Final</h2>

    <div class="border rounded-md p-4 bg-white shadow-sm">
      <!-- Foto -->
      <div v-if="store.foto" class="mb-4 flex justify-center">
        <img :src="store.foto" alt="Foto do usuário" class="w-24 h-24 rounded-full object-cover border shadow" />
      </div>

      <!-- Nome e dados -->
      <h3 class="text-xl font-semibold text-teal-700 text-center">{{ store.nome }}</h3>
      <p class="text-gray-600 text-sm text-center mt-1">
        <span v-if="store.idade">Idade: {{ store.idade }}</span>
        <span v-if="store.estadoCivil"> • Estado Civil: {{ store.estadoCivil }}</span><br />
        Email: {{ store.email }}<br />
        <span v-if="store.endereco">Endereço: {{ store.endereco }}</span><br />
        <span v-if="store.telefone">Telefone: {{ store.telefone }}</span>
      </p>

      <hr class="my-3" />

      <!-- Objetivo -->
      <p v-if="store.objetivo" class="mt-4"><strong>Objetivo</strong><br />{{ store.objetivo }}</p>

      <!-- Formação Acadêmica -->
      <div v-if="formacoesValidas.length">
        <h4 class="mt-4 font-semibold text-gray-700">Formação Acadêmica</h4>
        <ul class="list-disc list-inside text-sm text-gray-700">
          <li v-for="(f, i) in formacoesValidas" :key="i">
            {{ f.tipo }}
            <template v-if="f.nomeEscola"> – {{ f.nomeEscola }}</template>
            <template v-if="f.nomeCurso"> | Curso: {{ f.nomeCurso }}</template>
            <template v-if="f.inicio || f.fim"> ({{ f.inicio || '?' }} - {{ f.fim || '?' }})</template>
          </li>
        </ul>
      </div>

      <!-- Experiência Profissional -->
      <div class="mt-4">
        <h4 class="font-semibold text-gray-700">Experiência Profissional</h4>
        <p v-if="store.statusExperiencia === 'Em busca do primeiro emprego'" class="text-sm text-gray-600 mt-1">
          Estou em busca da minha primeira oportunidade profissional.
        </p>
        <div v-else-if="experienciasValidas.length">
          <p class="text-sm text-gray-600 mt-1">Já tive experiências anteriores nas seguintes empresas:</p>
          <ul class="list-disc list-inside text-sm text-gray-700 mt-2">
            <li v-for="(e, i) in experienciasValidas" :key="i">
              {{ e.cargo }} – {{ e.empresa }} ({{ e.periodo }})<br />
              <span class="text-xs text-gray-500">{{ e.atividades }}</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Habilidades -->
      <div v-if="store.habilidades.length">
        <h4 class="mt-4 font-semibold text-gray-700">Habilidades</h4>
        <div class="flex flex-wrap gap-2 mt-1">
          <span v-for="(h, i) in store.habilidades" :key="i" class="tag">{{ h }}</span>
        </div>
      </div>

      <!-- Idiomas -->
      <div v-if="store.idiomas.length">
        <h4 class="mt-4 font-semibold text-gray-700">Idiomas</h4>
        <div class="flex flex-wrap gap-2 mt-1">
          <span v-for="(i, index) in store.idiomas" :key="index" class="tag bg-blue-600">{{ i }}</span>
        </div>
      </div>

      <!-- Cursos -->
      <div v-if="store.cursos.length">
        <h4 class="mt-4 font-semibold text-gray-700">Cursos Complementares</h4>
        <div class="flex flex-wrap gap-2 mt-1">
          <span v-for="(c, i) in store.cursos" :key="i" class="tag bg-amber-600">{{ c }}</span>
        </div>
      </div>

      <!-- Disponibilidade -->
      <div v-if="store.disponibilidades.length">
        <h4 class="mt-4 font-semibold text-gray-700">Disponibilidade</h4>
        <div class="flex flex-wrap gap-2 mt-1">
          <span v-for="(d, i) in store.disponibilidades" :key="i" class="tag bg-indigo-600">{{ d }}</span>
        </div>
      </div>
    </div>

    <!-- Feedback -->
    <div class="text-center text-sm">
      <div v-if="carregando" class="text-gray-500 animate-pulse mt-2">
        ⏳ Carregando currículo...
      </div>
      <div v-if="sucesso && !carregando" class="text-green-600 font-semibold mt-2 animate-fade">
        ✅ Currículo gerado com sucesso!
      </div>
    </div>

    <!-- Botões -->
    <div class="flex justify-between mt-4">
      <button @click="$emit('voltar')" class="text-gray-600 hover:underline">Voltar e Editar</button>
      <button @click="gerarPdf" class="bg-green-600 hover:bg-green-700 text-white py-2 px-6 rounded-md font-semibold">
        Baixar PDF
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useCurriculoStore } from '../stores/curriculo'

const store = useCurriculoStore()

// Estados de feedback
const carregando = ref(false)
const sucesso = ref(false)

// Computeds para validação
const formacoesValidas = computed(() =>
  store.formacoes.filter(f => f.tipo)
)

const experienciasValidas = computed(() =>
  store.experiencias.filter(e => e.empresa && e.cargo && e.periodo)
)

// Gera e baixa o PDF
const gerarPdf = async () => {
  carregando.value = true
  sucesso.value = false

  try {
    const response = await fetch('https://curriculoplus.onrender.com/gerar-pdf', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(store.$state)
    })

    if (!response.ok) throw new Error('Erro ao gerar PDF')

    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `curriculo-${store.nome?.replace(/\s+/g, '-') || 'documento'}.pdf`
    document.body.appendChild(a)
    a.click()
    a.remove()
    window.URL.revokeObjectURL(url)

    sucesso.value = true
  } catch (error) {
    console.error('Erro ao gerar PDF:', error)
    alert('Erro ao gerar PDF. Verifique sua conexão com o servidor.')
  } finally {
    carregando.value = false
  }
}
</script>

<style scoped>
.tag {
  @apply text-white px-3 py-1 rounded-full text-sm bg-teal-600;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: scale(0.95);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-fade {
  animation: fadeIn 0.7s ease-out;
}
</style>

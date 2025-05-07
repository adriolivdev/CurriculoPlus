import { defineStore } from 'pinia'

export const useCurriculoStore = defineStore('curriculo', {
  state: () => ({
    nome: '',
    email: '',
    endereco: '',
    telefone: '',
    idade: '',
    estadoCivil: '',
    foto: null,

    nivel: '',
    area: '',
    objetivo: '',
    formacoes: [
      {
        tipo: '',
        nomeEscola: '',
        nomeCurso: '',
        inicio: '',
        fim: ''
      }
    ],

    statusExperiencia: '',
    experiencias: [
      { empresa: '', cargo: '', periodo: '', atividades: '' },
      { empresa: '', cargo: '', periodo: '', atividades: '' },
      { empresa: '', cargo: '', periodo: '', atividades: '' }
    ],

    habilidades: [],
    idiomas: [],
    cursos: [],
    disponibilidades: []
  }),

  actions: {
    atualizar(dados) {
      Object.assign(this, dados)
    },
    resetar() {
      this.$reset()
    }
  }
})

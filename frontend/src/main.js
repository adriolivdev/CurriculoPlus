import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

// ⚠️ IMPORTANTE: importar e usar o Pinia
import { createPinia } from 'pinia'

const app = createApp(App)

app.use(createPinia()) // ← isso ativa o Pinia no seu app
app.mount('#app')

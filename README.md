# 📄 Currículo+

O **Currículo+** é uma aplicação web responsiva para criação de currículos modernos e acessíveis, com opção de exportar para PDF, suporte a foto e preenchimento guiado por etapas.

Desenvolvido com foco em usabilidade, acessibilidade e automação inteligente de conteúdo (como objetivo profissional dinâmico baseado em cargo e área).

---

## 🚀 Tecnologias Utilizadas

### Front-end (Vue 3 + Vite + Tailwind CSS)
- `Vue 3` com Composition API
- `Pinia` para gerenciamento de estado global
- `Tailwind CSS` v3.3.2 para estilização responsiva e utilitária
- `Vite` para build ultra rápido

### Back-end (Python + Flask)
- `Flask` para API REST
- `pdfkit` + `wkhtmltopdf` para geração de PDF com HTML renderizado
- `CORS` para conexão segura com o frontend

---

## 🧩 Funcionalidades

- [x] Formulário em etapas (step-by-step)
- [x] Upload de foto com preview (renderiza no PDF)
- [x] Objetivo profissional gerado automaticamente com base em seleção de cargo e área
- [x] Campos editáveis, com visualização em tempo real (preview)
- [x] Geração de PDF com layout limpo e profissional
- [x] Lista de habilidades, idiomas, cursos e disponibilidade com seleção visual por tag
- [x] Validações dinâmicas e responsividade

---

## 📦 Instalação e Execução Local

### 1. Clonar o projeto
```bash
git clone https://github.com/seu-usuario/curriculo-plus.git
cd curriculo-plus
```

### 2. Rodar o Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Rodar o Backend (API Flask)
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python utils/app.py
```

**Certifique-se de ter o `wkhtmltopdf` instalado em:**
```
C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe
```
Ou altere o caminho no `app.py`.

---

## 🖼️ Estrutura de Diretórios

```
curriculo-plus/
├── frontend/                 # App Vue 3 + Tailwind + Pinia
│   ├── components/
│   ├── stores/
│   ├── App.vue
│   └── main.js
├── backend/
│   └── utils/
│       └── app.py           # Flask API com PDFKit
├── README.md
```

---

## ✨ Screenshots

<img src="/screenshots/formulario.png" alt="Formulário" />
<img src="/screenshots/preview.png" alt="Preview" />
<img src="/screenshots/pdf.png" alt="PDF" />

---

## 🧠 Autor

Desenvolvido por [**adriolivdev </>**](https://github.com/adriolivdev) 💚

---

## 📌 Roadmap Futuro

- [ ] Opção de salvar e carregar dados com localStorage
- [ ] Modo escuro (dark mode)
- [ ] Tema personalizável para o PDF
- [ ] Suporte a exportação em outros formatos (Word, JSON)

---

## 🪄 Deploy Sugerido

- **Frontend:** [Vercel](https://vercel.com/) ou [Netlify](https://www.netlify.com/)
- **Backend (Flask):** [Render](https://render.com/) ou [Replit](https://replit.com/)

---

## 📝 Licença

Este projeto é livre para fins educacionais e pessoais. Distribuições comerciais devem citar a autora original.

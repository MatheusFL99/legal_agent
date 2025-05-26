# 🤖 JusAI – Assistente Jurídico com IA

O **JusAI** é um sistema inteligente de perguntas e respostas jurídicas desenvolvido com **Typescript ( Next.js para frontend)** e **Python (FastAPI para o backend)**. Ele utiliza modelos de linguagem (LLMs) integrados à API do **OpenRouter (modelo Gemini)** para fornecer respostas com base em legislações brasileiras.

---

## 🧠 Funcionalidades

- ✅ Interface de chatbot moderna.
- ✅ Respostas geradas por IA em português do Brasil.
- ✅ Sugestão de links relevantes de fontes públicas jurídicas.
- ✅ Armazenamento de histórico de consultas no MongoDB.
- ✅ Integração com fontes externas.
- ✅ **Contexto de sessão:** a IA utiliza perguntas e respostas anteriores da mesma sessão para manter o raciocínio e dar respostas mais coerentes.
- ✅ Layout responsivo..

---

## 🧱 Tecnologias Utilizadas

| Frontend     | Backend         | IA & Dados          |
| ------------ | --------------- | ------------------- |
| Next.js 14   | FastAPI         | OpenRouter (Gemini) |
| TypeScript   | Python 3.11+    | MongoDB Atlas       |
| Tailwind CSS | Uvicorn         | RAG Tools           |
| React        | CORS Middleware |                     |

---

## 🧪 Requisitos

- Node.js v18+
- Python 3.11+
- MongoDB Atlas (ou local)
- Chave de API do [OpenRouter](https://openrouter.ai/)

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/MatheusFL99/legal_agent.git
cd legal_agent
```

### 2. Backend (FastAPI)

```bash
cd api_server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

A API estará em `http://localhost:8000`.

### 3. Frontend (Next.js)

```bash
cd ../frontend
npm install
npm run dev
```

O frontend estará em `http://localhost:3000`

---

## 💡 Exemplo de Uso

- Usuário: "Quais são os meus direitos em caso de demissão sem justa causa?"
- IA: Explica os artigos da CLT e mostra links para Planalto, Jusbrasil etc.
- Usuário: "E se for por justa causa?"
- IA: Compreende o contexto da sessão e responde com base na continuidade.

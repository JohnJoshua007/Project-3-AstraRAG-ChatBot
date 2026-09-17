# 🤖 AstraRAG – Agentic RAG Chatbot

AstraRAG is an agentic Retrieval‑Augmented Generation (RAG) chatbot that answers questions grounded strictly in your uploaded documents — with source citations, tool transparency, and reasoning rationale for every answer. Built with CrewAI, LlamaIndex, ChromaDB, and Groq for blazing‑fast inference, with a clean Streamlit frontend and a FastAPI backend.

✨ Features

🧠 Agentic RAG – Uses CrewAI agents to reason about queries and invoke a retrieval tool.

📄 Document‑Grounded Answers – No hallucination; answers come only from your knowledge base.

📎 Source Attribution – Every answer lists the source files it used.

🔍 Full Transparency – Expand any answer to see the tool used and the agent's rationale.

⚡ Groq‑Powered Inference – Lightning‑fast LLM responses.

🗂️ ChromaDB Vector Store – Persistent, local, and fast.

🖥️ Modern Streamlit UI – Dark themed, responsive, and user‑friendly.

🔌 FastAPI Backend – Separates RAG logic from the UI; can be reused by other clients.

📥 Simple Ingestion Pipeline – Drop PDFs into a folder and run one command.


🚀 Quick Start

1. Clone the repository

git clone https://github.com/JohnJoshua007/Project-3-AstraRAG-ChatBot.git

cd Project-3-AstraRAG-ChatBot


2. Create a virtual environment

python -m venv .venv

.\.venv\Scripts\activate         # Windows

source .venv/bin/activate        # Linux / macOS


3. Install dependencies

pip install -r requirements.txt


4. Set up environment variables

Create a .env file in the project root:

# Groq API

GROQ_API_KEY=your_groq_api_key_here

# Document ingestion

DOCUMENTS_DIR=./data

VECTOR_STORE_DIR=./doc_vector_store

COLLECTION_NAME=astra_docs

# Frontend

CHAT_ENDPOINT_URL=http://localhost:8000/chat/answer

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


🏗️ Architecture

┌─────────────────┐      HTTP POST       ┌──────────────────────┐
│  Streamlit UI   │  ─────────────────▶  │   FastAPI Backend    │
│  (frontend)     │                      │   /chat/answer       │
└─────────────────┘                      └──────────┬───────────┘
                                                    │
                                                    ▼
                                         ┌──────────────────────┐
                                         │   CrewAI Agent       │
                                         │  (Question Answer)   │
                                         └──────────┬───────────┘
                                                    │ calls
                                                    ▼
                                         ┌──────────────────────┐
                                         │  rag_query_tool      │
                                         │  (vector retrieval + │
                                         │   LLM synthesis)     │
                                         └──────────┬───────────┘
                                                    │
                                                    ▼
                                         ┌──────────────────────┐
                                         │   ChromaDB +         │
                                         │   HuggingFace        │
                                         │   Embeddings         │
                                         └──────────────────────┘

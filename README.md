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


🧪 Usage

Type a question like:

"What is an ecosystem?"

"Explain the difference between evolution and ecosystem."

"Summarise chapter 3."

Read the grounded answer.

Expand 🔍 Show details (tool & rationale) to see:

Which tool was used (rag_query_tool)

The agent's reasoning

The source files cited

Follow‑up questions retain the conversation context.




COLLECTION_NAME=astra_docs

# Frontend

CHAT_ENDPOINT_URL=http://localhost:8000/chat/answer

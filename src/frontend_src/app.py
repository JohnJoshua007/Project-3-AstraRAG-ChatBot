# import sys
# import os
# # Add project root to sys.path BEFORE any imports
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#
# import streamlit as st
# import requests
# from src.frontend_src.config.frontend_settings import Settings
#
# settings = Settings()
#
# st.set_page_config(
#     page_title="AstraRAG",
#     page_icon="🤖",
#     layout="centered",
# )
# st.title("💬 AstraRAG - Agentic RAG Chatbot")
#
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
#
# for message in st.session_state.chat_history:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#         if message.get("role") == "assistant":
#             sources = message.get("sources", [])
#             tool_used = message.get("tool_used")
#             rationale = message.get("rationale")
#             if sources:
#                 st.markdown(f"**Sources:** {', '.join(sources)}")
#             if tool_used or rationale:
#                 with st.expander("Show details (tool & rationale)"):
#                     st.markdown(f"**Tool Used:** {tool_used if tool_used else 'N/A'}")
#                     st.markdown(f"**Rationale:** {rationale if rationale else 'N/A'}")
#
# user_prompt = st.chat_input("Ask Chatbot...")
#
# if user_prompt:
#     st.chat_message("user").markdown(user_prompt)
#     st.session_state.chat_history.append({"role": "user", "content": user_prompt})
#
#     # Prepare payload for API
#     payload = {"chat_history": st.session_state.chat_history}
#     try:
#         response = requests.post(settings.CHAT_ENDPOINT_URL, json=payload)
#         response.raise_for_status()
#         response_json = response.json()
#         assistant_response = response_json.get("answer", "(No response)")
#         tool_used = response_json.get("tool_used", "N/A")
#         rationale = response_json.get("rationale", "N/A")
#         sources = response_json.get("sources", [])
#     except Exception as e:
#         assistant_response = f"Error: {e}"
#         tool_used = "N/A"
#         rationale = "N/A"
#         sources = []
#
#     st.session_state.chat_history.append({
#         "role": "assistant",
#         "content": assistant_response,
#         "tool_used": tool_used,
#         "rationale": rationale,
#         "sources": sources
#     })
#     with st.chat_message("assistant"):
#         st.markdown(assistant_response)
#         if sources:
#             st.markdown(f"**Sources:** {', '.join(sources)}")
#         with st.expander("Show details (tool & rationale)"):
#             st.markdown(f"**Tool Used:** {tool_used}")
#             st.markdown(f"**Rationale:** {rationale}")



import sys
import os

# Add project root to sys.path BEFORE any imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
import requests
from src.frontend_src.config.frontend_settings import Settings

settings = Settings()

# ---------- Page config ----------
st.set_page_config(
    page_title="AstraRAG",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------- Custom CSS (soft dark theme) ----------
st.markdown(
    """
    <style>
    /* Global font */
    html, body, [class*="css"] {
        font-family: 'Inter', 'Segoe UI', sans-serif;
        color: #e2e8f0;
    }

    /* Main background - soft dark */
    .stApp {
        background: #111827;
    }

    /* Header card */
    .astra-header {
        background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 55%, #ec4899 100%);
        padding: 24px 28px;
        border-radius: 14px;
        margin-bottom: 20px;
        box-shadow: 0 6px 22px rgba(99, 102, 241, 0.35);
    }
    .astra-header h1 {
        margin: 0;
        color: #ffffff;
        font-size: 26px;
        font-weight: 700;
        letter-spacing: 0.2px;
    }
    .astra-header p {
        margin: 8px 0 0 0;
        color: #f1f5f9;
        font-size: 14px;
        line-height: 1.4;
    }

    /* Chat message container */
    [data-testid="stChatMessage"] {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
    }

    /* Chat message text */
    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] span {
        color: #e2e8f0 !important;
        font-size: 15px;
        line-height: 1.55;
    }

    /* Source chips */
    .source-chip {
        display: inline-block;
        background: rgba(99, 102, 241, 0.18);
        color: #a5b4fc;
        border: 1px solid rgba(99, 102, 241, 0.45);
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 12.5px;
        font-weight: 500;
        margin: 4px 6px 4px 0;
    }

    /* Meta badge (tool) */
    .meta-badge {
        display: inline-block;
        background: rgba(236, 72, 153, 0.18);
        color: #f9a8d4;
        border: 1px solid rgba(236, 72, 153, 0.45);
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 12.5px;
        font-weight: 500;
        margin-bottom: 8px;
    }

    /* Welcome card */
    .welcome-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px 24px;
        margin-bottom: 18px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
    }
    .welcome-card h3 {
        margin: 0 0 12px 0;
        color: #a5b4fc;
        font-size: 17px;
        font-weight: 600;
    }
    .welcome-row {
        background: rgba(99, 102, 241, 0.08);
        border-left: 3px solid #6366f1;
        border-radius: 6px;
        padding: 10px 14px;
        margin-bottom: 10px;
        color: #cbd5e1;
        font-size: 14px;
        line-height: 1.5;
    }
    .welcome-row:last-child {
        margin-bottom: 0;
    }
    .welcome-row em {
        color: #e2e8f0;
        font-style: italic;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #0f172a;
        border-right: 1px solid #1e293b;
    }
    [data-testid="stSidebar"] * {
        color: #cbd5e1 !important;
    }
    [data-testid="stSidebar"] h3 {
        color: #a5b4fc !important;
        font-size: 15px;
        font-weight: 600;
        margin-top: 12px;
    }
    [data-testid="stSidebar"] hr {
        margin: 14px 0;
        border-color: #1e293b;
    }
    [data-testid="stSidebar"] .stCaption {
        color: #94a3b8 !important;
    }

    /* Metric labels */
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-size: 13px !important;
    }
    [data-testid="stMetricValue"] {
        color: #a5b4fc !important;
        font-size: 22px !important;
        font-weight: 700 !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: #ffffff !important;
        border: none;
        border-radius: 10px;
        padding: 10px 16px;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s ease;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 18px rgba(139, 92, 246, 0.45);
        color: #ffffff !important;
    }

    /* Chat input */
    [data-testid="stChatInput"] textarea {
        background: #1e293b !important;
        color: #e2e8f0 !important;
        border-radius: 12px;
        border: 1px solid #334155;
        font-size: 15px;
    }
    [data-testid="stChatInput"] textarea::placeholder {
        color: #64748b !important;
    }

    /* Expander */
    details {
        background: #0f172a;
        border-radius: 10px;
        border: 1px solid #1e293b;
        padding: 8px 14px;
        margin-top: 8px;
    }
    details summary {
        color: #a5b4fc;
        font-weight: 600;
        font-size: 13.5px;
        cursor: pointer;
    }
    details p, details span {
        color: #cbd5e1 !important;
        font-size: 13.5px;
    }

    /* Alert boxes */
    [data-testid="stAlert"] {
        border-radius: 10px;
        font-size: 14px;
    }

    /* Reduce top padding of main content */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 820px;
    }

    /* Paragraph spacing inside chat */
    [data-testid="stChatMessage"] .stMarkdown p {
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Header ----------
st.markdown(
    """
    <div class="astra-header">
        <h1>💬 AstraRAG · Agentic RAG Chatbot</h1>
        <p>Ask anything from your knowledge base — grounded answers with sources, tools &amp; rationale.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Session state ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("### ⚙️ Controls")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")

    st.markdown("### 📊 Session Stats")
    user_msgs = sum(1 for m in st.session_state.chat_history if m["role"] == "user")
    ai_msgs = sum(1 for m in st.session_state.chat_history if m["role"] == "assistant")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("You", user_msgs)
    with col2:
        st.metric("AI", ai_msgs)

    st.markdown("---")

    st.markdown("### ℹ️ About")
    st.caption(
        "AstraRAG combines vector retrieval with an agentic LLM workflow. "
        "Every answer is grounded in your uploaded documents and cites its sources."
    )

# ---------- Welcome card (3 rows) ----------
if not st.session_state.chat_history:
    st.markdown(
        """
        <div class="welcome-card">
            <h3>👋 Welcome to AstraRAG!</h3>
            <div class="welcome-row">💡 Try asking: <em>"What is an ecosystem?"</em></div>
            <div class="welcome-row">🧠 Try asking: <em>"Explain the difference between evolution and ecosystem."</em></div>
            <div class="welcome-row">📄 Try asking: <em>"Summarise the main points from chapter 3."</em></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- Render chat history ----------
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("role") == "assistant":
            sources = message.get("sources", [])
            tool_used = message.get("tool_used")
            rationale = message.get("rationale")

            if sources:
                chips = "".join(
                    f'<span class="source-chip">📄 {s}</span>' for s in sources
                )
                st.markdown(
                    f"**Sources:**&nbsp; {chips}", unsafe_allow_html=True
                )

            if tool_used or rationale:
                with st.expander("🔍 Show details (tool & rationale)"):
                    st.markdown(
                        f'<span class="meta-badge">🛠️ Tool: {tool_used or "N/A"}</span>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"**🧠 Rationale:** {rationale or 'N/A'}")

# ---------- Chat input ----------
user_prompt = st.chat_input("Ask AstraRAG anything...")

if user_prompt:
    # Show user message immediately
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Prepare payload
    payload = {"chat_history": st.session_state.chat_history}

    # Assistant message with spinner
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("_🤔 Thinking… retrieving documents and reasoning…_")

        try:
            response = requests.post(
                settings.CHAT_ENDPOINT_URL,
                json=payload,
                timeout=120,
            )
            response.raise_for_status()
            response_json = response.json()

            assistant_response = response_json.get("answer", "(No response)")
            tool_used = response_json.get("tool_used", "N/A")
            rationale = response_json.get("rationale", "N/A")
            sources = response_json.get("sources", [])

        except requests.exceptions.Timeout:
            assistant_response = "⏱️ Request timed out. The model took too long to respond."
            tool_used, rationale, sources = "N/A", "N/A", []
        except requests.exceptions.ConnectionError:
            assistant_response = (
                "🔌 Could not connect to the backend server. "
                "Make sure it's running on the configured endpoint."
            )
            tool_used, rationale, sources = "N/A", "N/A", []
        except Exception as e:
            assistant_response = f"❌ Error: {e}"
            tool_used, rationale, sources = "N/A", "N/A", []

        # Replace the placeholder with the real answer
        placeholder.markdown(assistant_response)

        if sources:
            chips = "".join(f'<span class="source-chip">📄 {s}</span>' for s in sources)
            st.markdown(f"**Sources:**&nbsp; {chips}", unsafe_allow_html=True)

        with st.expander("🔍 Show details (tool & rationale)"):
            st.markdown(
                f'<span class="meta-badge">🛠️ Tool: {tool_used or "N/A"}</span>',
                unsafe_allow_html=True,
            )
            st.markdown(f"**🧠 Rationale:** {rationale or 'N/A'}")

    # Persist assistant message
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_response,
        "tool_used": tool_used,
        "rationale": rationale,
        "sources": sources,
    })
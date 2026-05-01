import streamlit as st
import os
import tempfile
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Docnify – AI Document Reader",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --bg:       #0d0d14;
    --surface:  #16162a;
    --surface2: #1e1e35;
    --violet:   #7c3aed;
    --vlt:      #a78bfa;
    --cyan:     #06b6d4;
    --pink:     #ec4899;
    --green:    #10b981;
    --text:     #f0eeff;
    --muted:    #6b6b8a;
    --border:   #2e2e50;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text) !important;
}
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
.block-container {
    padding: 2rem 1.5rem !important;
    max-width: 780px !important;
}

/* ── Top nav bar ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 2.5rem;
    padding-bottom: 1.2rem;
    border-bottom: 1px solid var(--border);
}
.brand {
    display: flex; align-items: center; gap: 10px;
}
.brand-icon {
    width: 40px; height: 40px;
    background: linear-gradient(135deg, #7c3aed, #06b6d4);
    border-radius: 11px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.2rem;
    box-shadow: 0 4px 15px rgba(124,58,237,0.45);
}
.brand-name {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #a78bfa, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.nav-badge {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 0.3rem 0.9rem;
    font-size: 0.75rem;
    color: var(--muted);
}

/* ── Upload card ── */
.upload-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.75rem;
    margin-bottom: 1.5rem;
}
.upload-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--vlt);
    margin-bottom: 1rem;
    display: flex; align-items: center; gap: 8px;
}

/* ── Streamlit file uploader — force full visibility ── */
[data-testid="stFileUploader"] {
    background: var(--surface2) !important;
    border-radius: 12px !important;
    padding: 0 !important;
}
[data-testid="stFileUploaderDropzone"] {
    background: #12122a !important;
    border: 2px dashed #7c3aed !important;
    border-radius: 12px !important;
    padding: 1.5rem 1rem !important;
    text-align: center !important;
    min-height: 110px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
[data-testid="stFileUploaderDropzone"] * {
    color: #c4b8ff !important;
    font-size: 0.88rem !important;
}
[data-testid="stFileUploaderDropzone"] svg {
    fill: #7c3aed !important;
    width: 32px !important; height: 32px !important;
    margin-bottom: 0.5rem !important;
}
[data-testid="stFileUploaderDropzone"] button {
    background: #7c3aed !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-size: 0.83rem !important;
    font-weight: 600 !important;
    padding: 0.4rem 1.2rem !important;
    margin-top: 0.5rem !important;
    cursor: pointer !important;
    box-shadow: 0 3px 12px rgba(124,58,237,0.5) !important;
}
/* hide the label above the uploader (we show our own title) */
[data-testid="stFileUploader"] > label { display: none !important; }
[data-testid="stFileUploader"] > div:first-child { display: none !important; }
[data-testid="stFileUploader"] > div > label { display: none !important; }
/* remove any empty box rendered by collapsed label */
[data-testid="stWidgetLabel"] { display: none !important; }

/* ── Active doc pill ── */
.active-doc {
    background: linear-gradient(135deg, rgba(16,185,129,0.13), rgba(6,182,212,0.09));
    border: 1px solid rgba(16,185,129,0.4);
    border-radius: 10px;
    padding: 0.65rem 1rem;
    margin-top: 0.9rem;
    display: flex; align-items: center; gap: 10px;
    font-size: 0.83rem;
}
.active-doc .ad-icon { font-size: 1.1rem; }
.active-doc .ad-name { color: #6ee7b7; font-weight: 600; }
.active-doc .ad-meta { color: var(--muted); font-size: 0.75rem; }

/* ── Divider ── */
.grad-line {
    height: 1px;
    background: linear-gradient(90deg, #7c3aed, #06b6d4, transparent);
    border: none;
    margin: 1.5rem 0;
}

/* ── Chat area ── */
.chat-wrap {
    max-height: 52vh;
    overflow-y: auto;
    padding: 0.25rem 0;
    scroll-behavior: smooth;
    margin-bottom: 1rem;
}
.chat-wrap::-webkit-scrollbar { width: 4px; }
.chat-wrap::-webkit-scrollbar-thumb { background: var(--border); border-radius: 10px; }

.msg-row { display: flex; margin-bottom: 1rem; align-items: flex-end; gap: 0.55rem; }
.msg-row.user { flex-direction: row-reverse; }
.msg-row.ai   { flex-direction: row; }

.avatar {
    width: 30px; height: 30px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem; flex-shrink: 0;
}
.avatar.user { background: linear-gradient(135deg,#ec4899,#7c3aed); }
.avatar.ai   { background: linear-gradient(135deg,#7c3aed,#06b6d4); }

.bubble {
    max-width: 78%; padding: 0.7rem 1rem;
    border-radius: 16px; font-size: 0.91rem; line-height: 1.6;
}
.bubble.user {
    background: linear-gradient(135deg,#7c3aed,#5b21b6);
    color: #fff; border-bottom-right-radius: 4px;
    box-shadow: 0 4px 14px rgba(124,58,237,0.3);
}
.bubble.ai {
    background: var(--surface2); color: var(--text);
    border: 1px solid var(--border); border-bottom-left-radius: 4px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

/* ── Welcome state ── */
.welcome {
    text-align: center; padding: 2rem 1rem;
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 16px; margin-bottom: 1.5rem;
}
.welcome h3 {
    font-family: 'Syne', sans-serif; font-size: 1.15rem;
    color: var(--vlt); margin: 0.75rem 0 0.5rem;
}
.welcome p { color: var(--muted); font-size: 0.87rem; line-height: 1.6; }

/* ── Input row ── */
.stTextInput > div > div > input {
    background: var(--surface2) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-size: 0.92rem !important;
    padding: 0.65rem 1rem !important;
}
.stTextInput > div > div > input::placeholder { color: var(--muted) !important; }
.stTextInput > div > div > input:focus {
    border-color: var(--violet) !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.2) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg,#7c3aed,#06b6d4) !important;
    color: #fff !important; border: none !important;
    border-radius: 10px !important; font-weight: 600 !important;
    font-size: 0.88rem !important; padding: 0.6rem 1.2rem !important;
    box-shadow: 0 4px 14px rgba(124,58,237,0.35) !important;
    transition: opacity 0.2s, transform 0.15s !important;
}
.stButton > button:hover { opacity: 0.87 !important; transform: translateY(-1px) !important; }

/* secondary clear button */
.clear-btn > button {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    color: var(--muted) !important;
    box-shadow: none !important;
    font-size: 0.82rem !important;
}
.clear-btn > button:hover { border-color: var(--pink) !important; color: var(--pink) !important; }

/* ── Expander ── */
.stExpander {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: var(--violet) !important; }

/* ── Success / error ── */
.stAlert { background: var(--surface2) !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)


# ── Backend ───────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def get_embedding_model():
    from langchain_mistralai import MistralAIEmbeddings
    return MistralAIEmbeddings()

@st.cache_resource(show_spinner=False)
def get_llm():
    from langchain_mistralai import ChatMistralAI
    return ChatMistralAI(model="mistral-small-2506")

@st.cache_resource(show_spinner=False)
def get_prompt():
    from langchain_core.prompts import ChatPromptTemplate
    return ChatPromptTemplate.from_messages([
        ("system", """You are Docnify, a helpful AI document assistant.
Use ONLY the provided context to answer the question.
If the answer is not in the context, say: "I could not find the answer in the document." """),
        ("human", "Context:\n{context}\n\nQuestion:\n{question}")
    ])

def build_vectorstore(pdf_bytes, filename):
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import Chroma
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf_bytes); tmp_path = tmp.name
    docs   = PyPDFLoader(tmp_path).load()
    os.unlink(tmp_path)
    chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
    vs     = Chroma.from_documents(chunks, get_embedding_model(), persist_directory="chroma_db")
    os.makedirs("chroma_db", exist_ok=True)
    return vs, len(chunks), len(docs)


def ask(query, vectorstore):
    docs     = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k":4,"fetch_k":10,"lambda_mult":0.5}).invoke(query)
    context  = "\n\n".join(d.page_content for d in docs)
    response = get_llm().invoke(get_prompt().invoke({"context": context, "question": query}))
    return response.content, docs


# ── Session state ─────────────────────────────────────────────────────────────
for k, v in [("messages",[]), ("vectorstore", None), ("doc_name", None),
             ("chunk_count", None), ("page_count", None)]:
    if k not in st.session_state:
        st.session_state[k] = v

# Always start fresh — user must upload a new PDF each session


# ── Top bar ───────────────────────────────────────────────────────────────────
msgs_n = len([m for m in st.session_state.messages if m["role"] == "user"])
st.markdown(f"""
<div class="topbar">
  <div class="brand">
    <div class="brand-icon">✦</div>
    <span class="brand-name">Docnify</span>
  </div>
  <span class="nav-badge">✦ {msgs_n} question{"s" if msgs_n!=1 else ""} asked</span>
</div>
""", unsafe_allow_html=True)


# ── Upload card ───────────────────────────────────────────────────────────────
with st.container():
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown('<div class="upload-card-title">📂 Upload your PDF document</div>', unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "upload",
        type=["pdf"],
        label_visibility="collapsed",
        help="Upload any PDF book or document to chat with it"
    )

    if uploaded:
        st.markdown(f"""
<div style="background:#1a1a30;border:1px solid #2e2e50;border-radius:8px;
            padding:0.5rem 0.9rem;font-size:0.82rem;color:#a78bfa;margin-top:0.5rem;">
  📄 &nbsp;<strong>{uploaded.name}</strong>
  &nbsp;·&nbsp; <span style="color:#6b6b8a">{round(uploaded.size/1024,1)} KB</span>
</div>""", unsafe_allow_html=True)
        if st.button("⚡ Index Now", use_container_width=True):
            with st.spinner("Reading & embedding your document…"):
                try:
                    vs, nc, np_ = build_vectorstore(uploaded.read(), uploaded.name)
                    st.session_state.vectorstore = vs
                    st.session_state.doc_name    = uploaded.name
                    st.session_state.chunk_count = nc
                    st.session_state.page_count  = np_
                    st.session_state.messages    = []
                    st.success(f"✅ Done! {nc} chunks indexed from {np_} pages.")
                except Exception as e:
                    st.error(f"Error: {e}")

    if st.session_state.doc_name:
        meta = ""
        if st.session_state.page_count:  meta += f"📄 {st.session_state.page_count} pages &nbsp;·&nbsp; "
        if st.session_state.chunk_count: meta += f"🧩 {st.session_state.chunk_count} chunks"
        else: meta = "Ready to chat"
        st.markdown(f"""
<div class="active-doc">
  <span class="ad-icon">✅</span>
  <div>
    <div class="ad-name">{st.session_state.doc_name}</div>
    <div class="ad-meta">{meta}</div>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ── Chat section ──────────────────────────────────────────────────────────────
st.markdown('<hr class="grad-line">', unsafe_allow_html=True)

if not st.session_state.vectorstore:
    st.markdown("""
<div class="welcome">
  <div style="font-size:2rem">📚</div>
  <h3>Ready to chat with your document</h3>
  <p>Upload a PDF above and click <strong style="color:#a78bfa">⚡ Index Now</strong><br>
  Then ask any question about its contents.</p>
</div>""", unsafe_allow_html=True)
else:
    # Chat history
    if st.session_state.messages:
        chat_html = '<div class="chat-wrap">'
        for msg in st.session_state.messages:
            role  = msg["role"]
            emoji = "👤" if role == "user" else "✦"
            chat_html += f"""
<div class="msg-row {role}">
  <div class="avatar {role}">{emoji}</div>
  <div class="bubble {role}">{msg["content"]}</div>
</div>"""
        chat_html += '</div>'
        st.markdown(chat_html, unsafe_allow_html=True)

        # Source passages
        last = st.session_state.messages[-1]
        if last["role"] == "ai" and last.get("sources"):
            with st.expander(f"📎 {len(last['sources'])} source passages", expanded=False):
                for i, doc in enumerate(last["sources"], 1):
                    pg = doc.metadata.get("page", "?")
                    st.markdown(f"**Chunk {i}** — page {pg}")
                    st.caption(doc.page_content[:400] + ("…" if len(doc.page_content) > 400 else ""))
                    if i < len(last["sources"]): st.divider()
    else:
        st.markdown(f"""
<div class="welcome">
  <div style="font-size:2rem">💬</div>
  <h3>Start chatting!</h3>
  <p>Your document <strong style="color:#6ee7b7">{st.session_state.doc_name}</strong> is ready.<br>
  Ask anything below.</p>
</div>""", unsafe_allow_html=True)

    # Input
    col_q, col_s, col_c = st.columns([5, 1, 1])
    with col_q:
        user_query = st.text_input("q", placeholder="Ask anything about your document…",
                                   label_visibility="collapsed", key="query_input")
    with col_s:
        send = st.button("Send ✦", use_container_width=True)
    with col_c:
        st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
        if st.button("Clear", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    if send and user_query.strip():
        st.session_state.messages.append({"role": "user", "content": user_query.strip()})
        with st.spinner("Docnify is thinking…"):
            try:
                answer, sources = ask(user_query.strip(), st.session_state.vectorstore)
            except Exception as e:
                answer, sources = f"⚠️ Error: {e}", []
        st.session_state.messages.append({"role": "ai", "content": answer, "sources": sources})
        st.rerun()
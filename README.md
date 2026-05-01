# ✦ Docnify — AI Document Reader

Docnify is a **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and interact with them using natural language.

It extracts, indexes, and retrieves relevant content from documents to generate accurate, context-aware answers.

---

## 🚀 Features

* 📂 Upload any PDF and chat with it
* 🧠 Context-aware answers using **Mistral AI**
* 🔍 Semantic search powered by **ChromaDB**
* 💬 Chat interface with conversation history
* 📎 Source chunk visibility for transparency

---

## 🛠 Tech Stack

* **Frontend/UI**: Streamlit
* **LLM & Embeddings**: Mistral AI
* **Framework**: LangChain
* **Vector Database**: ChromaDB
* **Language**: Python

---

## 📁 Project Structure

```id="readme-structure"
docnify/
│
├── app.py              # Streamlit UI (file upload + chat)
├── main.py             # RAG backend logic (embedding + retrieval + LLM)
├── requirements.txt    # Dependencies
├── .gitignore          # Ignored files
└── README.md           # Project documentation
```

---

## ⚙️ How It Works

1. User uploads a PDF
2. Document is split into chunks
3. Chunks are converted into embeddings
4. Stored in a vector database (ChromaDB)
5. User asks a question
6. Relevant chunks are retrieved (MMR search)
7. LLM generates answer using only retrieved context

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/docnify.git
cd docnify
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```id="env-block"
MISTRAL_API_KEY=your_api_key_here
```

---

## ⚠️ Important Notes

* `chroma_db/` is auto-generated — do NOT upload it
* `.env` file should never be pushed to GitHub
* Designed for single-user session (not multi-user scalable yet)

---

## 📌 Limitations

* Database is overwritten on each new upload
* No long-term memory or multi-document support
* Not optimized for very large PDFs

---

## 🚀 Future Improvements

* Multi-document support
* Persistent user sessions
* Chat memory integration
* Deployment (Streamlit Cloud / Docker)
* Performance optimization for large files

---

## 👤 Author

**Yug Khatri**

---

## ⭐ If you found this useful

Consider giving this repository a star.

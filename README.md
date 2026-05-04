

# ✦ Docnify — AI Document Reader

Docnify is a **Retrieval-Augmented Generation (RAG) application** that enables users to upload PDF documents and interact with them using natural language.

It combines **semantic search + LLM reasoning** to generate accurate, context-aware answers grounded in document content.

> ⚠️ Responses are generated based on retrieved context and may require verification for critical use cases.

---

## 🚀 Live Demo

<p align="center">
  <a href="https://docnify-rag-reader-04.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/📄%20Try%20Docnify-Live%20Demo-green?style=for-the-badge&logo=streamlit" />
  </a>
</p>

---

## 🧠 Overview

Docnify implements a **RAG pipeline** where user queries are answered using only the most relevant parts of uploaded documents. This avoids hallucination and improves factual accuracy compared to standalone LLM responses.

---

## ⚙️ Features

* 📂 Upload PDF and interact via chat
* 🧠 Context-aware answers using **Mistral AI**
* 🔍 Semantic search with **ChromaDB vector store**
* 💬 Conversational interface with history
* 📎 Source chunk display for transparency
* ⚡ Fast retrieval using embedding-based similarity

---

## 🛠 Tech Stack

* **Frontend/UI:** Streamlit
* **LLM & Embeddings:** Mistral AI
* **Framework:** LangChain
* **Vector Database:** ChromaDB
* **Language:** Python

---

## 🔄 System Workflow

1. User uploads a PDF
2. Document is split into chunks
3. Each chunk is converted into embeddings
4. Stored in **ChromaDB**
5. User submits a query
6. Relevant chunks retrieved using similarity search (MMR)
7. LLM generates answer using retrieved context only

---

## 📂 Project Structure

```bash id="docnify1"
docnify/
│── app.py              # Streamlit UI (upload + chat)
│── main.py             # RAG pipeline logic
│── requirements.txt
│── .gitignore
│── README.md
```

---

## ⚡ Run Locally

```bash id="docnify2"
git clone https://github.com/your-username/docnify.git
cd docnify
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Environment Setup

Create a `.env` file:

```env id="docnify3"
MISTRAL_API_KEY=your_api_key_here
```

---

## 📌 Key Concepts Used

* **RAG (Retrieval-Augmented Generation)**
* **Embeddings & Vector Search**
* **Maximum Marginal Relevance (MMR)**
* **Prompt Engineering with Context Injection**

---

## ⚠️ Limitations

* Vector database resets per session (no persistence)
* Single-document workflow
* Limited performance on very large PDFs
* Not optimized for concurrent users

---

## 🔮 Future Improvements

* Multi-document retrieval system
* Persistent vector storage
* User session memory
* API-based deployment (Docker / FastAPI)
* Improved chunking and retrieval strategies

---

## 👨‍💻 Author

**Yug Khatri**

---

## ⭐ Support

If this project helped you, consider giving it a ⭐

---


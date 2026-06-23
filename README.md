# 📄 Document Intelligence Q&A System (RAG-based AI App)

## 🚀 Overview
This project is an AI-powered document question answering system built using Retrieval-Augmented Generation (RAG).  

Users can upload a PDF document and ask natural language questions to retrieve the most relevant information from the document.

---

## 🧠 How It Works
1. A PDF document is uploaded by the user  
2. The text is extracted and split into smaller chunks  
3. Each chunk is converted into embeddings using a Sentence Transformer model  
4. Embeddings are stored in a FAISS vector database  
5. When a user asks a question, it is also converted into embeddings  
6. The system retrieves the most similar text chunks and returns them as answers  

---

## ⚙️ Features
- PDF text extraction  
- Text chunking for efficient processing  
- Semantic search using embeddings  
- FAISS vector similarity search  
- Interactive web interface using Streamlit  

---

## 🛠️ Tech Stack
- Python  
- Streamlit  
- SentenceTransformers  
- FAISS  
- PyPDF  
- NumPy  

---

## 📦 Installation

```bash
pip install -r requirements.txt

---

🚀 Run the App
streamlit run app.py

---

## 📌 Example Use Cases
Chat with PDF documents
Study notes summarization support
Research paper exploration
Business document search system

---

## 🎯 Skills Demonstrated
Natural Language Processing (NLP)
Embedding models
Vector databases (FAISS)
RAG architecture
AI application development
End-to-end system design

---

## 👩‍💻 Author

Morufat Ganiu
Aspiring AI/Data Scientist

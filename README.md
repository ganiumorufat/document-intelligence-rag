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
```
---

## 🚀 Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

---

## 📌 Key Use Cases

* Chat with PDF documents using natural language
* Generate concise summaries of study materials and notes
* Explore and query research papers efficiently
* Search and retrieve information from business documents
* Build a knowledge assistant powered by Retrieval-Augmented Generation (RAG)

---

## 🎯 Technical Skills Demonstrated

* Natural Language Processing (NLP)
* Retrieval-Augmented Generation (RAG)
* Text Embeddings and Semantic Search
* Vector Databases (FAISS)
* Large Language Model (LLM) Integration
* Prompt Engineering
* AI Application Development
* End-to-End Machine Learning System Design

---

## 📈 Project Highlights

* Built an intelligent document question-answering system.
* Implemented semantic search using FAISS vector indexing.
* Integrated LLMs to generate context-aware responses.
* Developed an interactive web application with Streamlit.
* Applied modern RAG architecture to improve response accuracy and relevance.

---

## 👩‍💻 Author

**Morufat Ganiu**

Data Analyst | Aspiring AI & Data Scientist

Passionate about leveraging data, machine learning, and artificial intelligence to solve real-world problems and create impactful solutions.

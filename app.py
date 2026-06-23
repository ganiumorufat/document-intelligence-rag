import streamlit as st
from rag_pipeline import DocumentQA

st.title("📄 Document Q&A AI System")

qa = DocumentQA()

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = qa.load_pdf("temp.pdf")
    chunks = qa.split_text(text)
    qa.build_index(chunks)

    st.success("Document processed successfully!")

    question = st.text_input("Ask a question")

    if question:
        results = qa.search(question)

        st.subheader("Relevant Information:")
        for r in results:
            st.write(r)
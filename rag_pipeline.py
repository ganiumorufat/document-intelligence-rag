from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pypdf import PdfReader

class DocumentQA:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.chunks = []

    def load_pdf(self, file_path):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def split_text(self, text, chunk_size=500):
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    def build_index(self, chunks):
        self.chunks = chunks
        embeddings = self.model.encode(chunks)

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))

    def search(self, question, k=3):
        query_embedding = self.model.encode([question])
        _, indices = self.index.search(np.array(query_embedding), k)

        return [self.chunks[i] for i in indices[0]]
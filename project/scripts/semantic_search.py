from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
import numpy as np

print("Starting VTU semantic search demo...")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load VTU notes
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "vtu_notes" / "sample_notes.txt"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Chunking
def chunk_text(text, chunk_size=400, overlap=50):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunks.append(" ".join(words[start:end]))
        start += chunk_size - overlap
    return chunks

chunks = chunk_text(text)
print(f"Total chunks: {len(chunks)}")

# Generate embeddings
chunk_embeddings = model.encode(chunks)

# User query
query = input("\nEnter your VTU question: ")
query_embedding = model.encode([query])

# Semantic similarity search
scores = cosine_similarity(query_embedding, chunk_embeddings)[0]
top_k = 3
top_indices = np.argsort(scores)[-top_k:][::-1]

print("\nTop relevant results:\n")
for idx in top_indices:
    print("Score:", round(scores[idx], 3))
    print(chunks[idx][:500])
    print("-" * 60)
context = "\n".join([chunks[i] for i in top_indices])

print("\n--- RAG CONTEXT ---\n")
print(context)
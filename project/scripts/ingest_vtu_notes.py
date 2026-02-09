import requests
from sentence_transformers import SentenceTransformer
from pathlib import Path

print("Starting VTU notes ingestion...")

# Resolve base directory (project/)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "vtu_notes" / "sample_notes.txt"

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read VTU notes
with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print(f"Loaded text length: {len(text)} characters")

# Simple chunking
def chunk_text(text, chunk_size=400, overlap=50):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

chunks = chunk_text(text)

print(f"Total chunks created: {len(chunks)}")
print(f"Total chunks created: {len(chunks)}")

# Generate embeddings
embeddings = model.encode(chunks)

# Insert into Endee
for i, (chunk, vector) in enumerate(zip(chunks, embeddings)):
    payload = {
        "index_name": "vtu_notes",
        "id": f"chunk_{i}",
        "vector": vector.tolist(),
        "metadata": {
            "text": chunk
        }
    }

    response = requests.put(
    "http://localhost:8080/api/v1/vector",
    json=payload
      )

    if response.status_code != 200:
        print(f"Error inserting chunk {i}: {response.text}")

print("Ingestion completed.")

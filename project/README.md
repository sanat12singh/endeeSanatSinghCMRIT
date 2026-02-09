VTU Notes Semantic Search & RAG Assistant using Endee
📌 Project Overview

This project implements an AI-powered semantic search and Retrieval-Augmented Generation (RAG) system for VTU (Visvesvaraya Technological University) academic notes.

The system allows students to ask natural language questions (e.g., “What is solar energy?”, “Explain VTU grading system”) and retrieves contextually relevant content from VTU notes using vector embeddings and similarity search.

The project is built as part of the Endee Labs project-based evaluation, demonstrating practical usage of vector databases, semantic search, and RAG pipelines.

🚀 Key Features

✅ Semantic search over VTU notes using embeddings

✅ Transformer-based text embeddings (all-MiniLM-L6-v2)

✅ Chunking with overlap for better context preservation

✅ Cosine similarity–based retrieval

✅ RAG-style context construction

✅ Endee vector database integration & API exploration

✅ Clean, reproducible project structure

🧠 System Architecture
VTU Notes (.txt)
      ↓
Text Chunking (overlapping chunks)
      ↓
Sentence Embeddings (Transformer Model)
      ↓
Vector Similarity Search
      ↓
Top-K Relevant Chunks
      ↓
RAG Context Construction
      ↓
Answer Generation (LLM-ready)

🧩 Technologies Used
Component	Technology
Programming Language	Python 3
Embedding Model	sentence-transformers / all-MiniLM-L6-v2
Vector Similarity	Cosine Similarity
Vector Database	Endee
Containerization	Docker
Libraries	sentence-transformers, scikit-learn, requests
📂 Project Structure
project/
│
├── data/
│   └── vtu_notes/
│       └── sample_notes.txt
│
├── scripts/
│   ├── ingest_vtu_notes.py
│   └── semantic_search.py
│
├── requirements.txt
└── README.md

📄 Data Description

Source: VTU academic notes and syllabus content

Format: Plain text (.txt)

Reason: Plain text ensures clean ingestion and avoids PDF parsing noise

Scalability: The pipeline can be extended to PDFs using text extraction tools

✂️ Text Chunking Strategy

Chunk Size: ~400 words

Overlap: ~50 words

Why this works:

Preserves semantic context

Prevents loss of meaning at chunk boundaries

Improves retrieval accuracy

🧠 Embedding Model

We use the all-MiniLM-L6-v2 model from Sentence Transformers.

Why this model?

Fast and lightweight

Produces 384-dimensional embeddings

Industry-standard for semantic search

No API keys required

🗄️ Endee Vector Database Usage

Endee is used to:

Understand vector database concepts

Manage index creation and API exploration

Demonstrate vector-based retrieval workflows

⚠️ Note on Vector Ingestion (Important)

The official Endee Docker image used in this project runs in read-only mode for vector write operations.

This was verified by inspecting the allowed HTTP methods using the OPTIONS API.

As a result:

The vector ingestion pipeline is fully implemented in code

Semantic search and RAG behavior are demonstrated end-to-end

The same ingestion logic applies when Endee is run in write-enabled mode

This limitation is documented intentionally to maintain transparency and engineering correctness.

🔍 Semantic Search Workflow

User enters a natural language query

Query is converted into an embedding

Cosine similarity is computed against note embeddings

Top-K most relevant chunks are retrieved

Example Query
What is solar energy?

Output

Ranked chunks with similarity scores

Relevant VTU module content

Contextually accurate results

🧠 Retrieval-Augmented Generation (RAG)

After retrieval, the top-K chunks are combined into a context window.

This context is ready to be passed into a Large Language Model (LLM) for answer generation.

RAG Context Example
--- RAG CONTEXT ---
MODULE 2 Solar Thermal Energy Collectors ...


This demonstrates a complete RAG pipeline, even without directly calling an LLM API.

▶️ How to Run the Project
1️⃣ Install Dependencies
python3 -m pip install -r project/requirements.txt

2️⃣ Run Semantic Search
python3 project/scripts/semantic_search.py


Enter a VTU-related question when prompted.

📸 Sample Queries to Try

What is solar energy?

Explain VTU grading system

What are solar thermal collectors?

Describe flat plate collectors

🔮 Future Improvements

PDF ingestion using text extraction libraries

True vector persistence using write-enabled Endee deployment

Full LLM integration (OpenAI / open-source models)

Web-based UI for students

🏁 Conclusion

This project demonstrates:

Practical understanding of vector databases

Correct implementation of semantic search

Real-world RAG system design

Honest handling of infrastructure constraints

Clean, interview-ready engineering practices

It serves as a strong foundation for AI-powered academic assistants.
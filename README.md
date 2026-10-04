# DevOps Vector Database & Semantic Search

A practical project for learning and implementing **Embeddings, Vector Databases, Semantic Search, and DevOps-focused AI applications** using Python, Ollama, and ChromaDB.

## 🚀 Project Overview

This repository contains my hands-on learning and implementation of vector databases and semantic search.

The project demonstrates how DevOps-related documents can be converted into embeddings, stored in a vector database, and searched using semantic similarity.

## 📂 Repository Structure

```text
vector-db-practice/
│
├── chroma_test.py
├── embedding_test.py
├── store_embeddings.py
├── search.py
├── metadata_test.py
├── metadata_search.py
├── crud_test.py
│
└── devops-semantic-search/
    ├── app.py
    ├── requirements.txt
    └── .gitignore
```

## 🧠 Technologies Used

* Python
* Ollama
* `nomic-embed-text`
* ChromaDB
* Vector Embeddings
* Semantic Search
* Metadata Filtering
* CRUD Operations

## 🔍 What I Learned

* What embeddings are
* How text is converted into vectors
* Vector dimensions
* Semantic similarity
* Similarity search
* Top-K search
* Using Ollama to generate embeddings
* Storing embeddings in ChromaDB
* Searching vectors using ChromaDB
* Metadata filtering
* CRUD operations in a vector database
* Building a DevOps-focused semantic search application

## ⚙️ How It Works

```text
DevOps Document
      ↓
Ollama Embedding Model
      ↓
Embedding Vector
      ↓
ChromaDB
      ↓
Semantic Similarity Search
      ↓
Relevant DevOps Information
```

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone <https://github.com/napanandavardhannaidu-collab/devops-vector-database-semantic-search>
cd vector-db-practice
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Make sure Ollama is installed and running

Check:

```bash
ollama --version
```

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

## ▶️ Running the Examples

Individual learning examples can be executed using:

```bash
python3 embedding_test.py
```

```bash
python3 store_embeddings.py
```

```bash
python3 search.py
```

```bash
python3 metadata_test.py
```

```bash
python3 metadata_search.py
```

```bash
python3 crud_test.py
```

## 🔎 DevOps Semantic Search

The `devops-semantic-search` directory contains the practical application.

It demonstrates semantic searching over DevOps-related information using:

```text
User Query
    ↓
Embedding Generation
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Relevant Results
```

## 🎯 Future Scope

The next stage of this learning journey is **Retrieval-Augmented Generation (RAG)**.

Future improvements can include:

* RAG
* LLM integration
* DevOps documentation assistant
* Log analysis
* AI-powered troubleshooting
* AI DevOps Agent
* Automated DevOps workflows

## 📚 Learning Roadmap

```text
LLM APIs
   ↓
Ollama
   ↓
Prompt Engineering
   ↓
Embeddings
   ↓
Vector Database
   ↓
RAG
   ↓
MCP
   ↓
AI Agents
   ↓
LangChain
   ↓
LangGraph
   ↓
AI-Powered DevOps
   ↓
Final AI DevOps Agent
```

## 👨‍💻 Author

**Nanda Vardhan**

B.Tech CSE / Computer Engineering - AI&ML

Interested in **DevOps, Cloud, AI, and AI-powered DevOps Automation**.

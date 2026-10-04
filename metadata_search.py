import chromadb
import ollama

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Get collection
collection = client.get_collection(
    name="devops_metadata"
)

# User query
query = "Which deployment failed?"

# Convert query to embedding
response = ollama.embed(
    model="nomic-embed-text",
    input=query
)

query_embedding = response["embeddings"][0]

# Search with metadata filter
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2,
    where={
        "environment": "production"
    }
)

print("Documents:")
print(results["documents"])

print("\nMetadata:")
print(results["metadatas"])

print("\nDistances:")
print(results["distances"])

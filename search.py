import chromadb
import ollama

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="devops_embeddings"
)

query = "How can I check Kubernetes pods?"

response = ollama.embed(
    model="nomic-embed-text",
    input=query
)

query_embedding = response["embeddings"][0]

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print("Documents:")
print(results["documents"])

print("\nDistances:")
print(results["distances"])

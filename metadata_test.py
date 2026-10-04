import chromadb
import ollama

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="devops_metadata"
)

documents = [
    "Docker container failed to start.",
    "Kubernetes pod is running successfully.",
    "Jenkins deployment failed during the build stage."
]

ids = ["log1", "log2", "log3"]

metadatas = [
    {
        "service": "docker",
        "environment": "development",
        "severity": "error"
    },
    {
        "service": "kubernetes",
        "environment": "production",
        "severity": "info"
    },
    {
        "service": "jenkins",
        "environment": "production",
        "severity": "error"
    }
]

response = ollama.embed(
    model="nomic-embed-text",
    input=documents
)

embeddings = response["embeddings"]

collection.add(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)

print("Documents with metadata stored!")
print("Total documents:", collection.count())

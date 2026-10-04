import chromadb
import ollama

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Create a new collection
collection = client.get_or_create_collection(
    name="devops_embeddings"
)

# Documents
documents = [
    "Docker containers can be started using the docker start command.",
    "Kubernetes pods can be inspected using the kubectl get pods command.",
    "Jenkins pipelines can be used to automate CI/CD workflows."
]

ids = ["doc1", "doc2", "doc3"]

# Generate embeddings using Ollama
response = ollama.embed(
    model="nomic-embed-text",
    input=documents
)

embeddings = response["embeddings"]

# Store everything in ChromaDB
collection.add(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=[
        {
            "service": "docker",
            "environment": "development",
            "severity": "info"
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
)

print("Documents and embeddings stored successfully!")
print("Total documents:", collection.count())

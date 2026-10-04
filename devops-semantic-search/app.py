import chromadb
import ollama

# -------------------------
# 1. Connect to ChromaDB
# -------------------------

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="devops_docs"
)

# -------------------------
# 2. DevOps documents
# -------------------------

documents = [
    "Docker containers can be started using the docker start command.",
    "Docker containers can be stopped using the docker stop command.",
    "Kubernetes pods can be inspected using kubectl get pods.",
    "Kubernetes pod logs can be viewed using kubectl logs.",
    "Jenkins pipelines automate continuous integration and continuous deployment.",
    "Jenkins pipeline failures can be investigated from the console output.",
    "AWS EC2 provides virtual servers in the cloud.",
    "Terraform is an Infrastructure as Code tool used to provision infrastructure."
]

ids = [
    "doc1",
    "doc2",
    "doc3",
    "doc4",
    "doc5",
    "doc6",
    "doc7",
    "doc8"
]

metadatas = [
    {"topic": "docker"},
    {"topic": "docker"},
    {"topic": "kubernetes"},
    {"topic": "kubernetes"},
    {"topic": "jenkins"},
    {"topic": "jenkins"},
    {"topic": "aws"},
    {"topic": "terraform"}
]

# -------------------------
# 3. Generate embeddings
# -------------------------

response = ollama.embed(
    model="nomic-embed-text",
    input=documents
)

embeddings = response["embeddings"]

# -------------------------
# 4. Store documents
# -------------------------

collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)

# -------------------------
# 5. Ask user for query
# -------------------------

query = input("\nEnter your DevOps question: ")

# -------------------------
# 6. Embed query
# -------------------------

response = ollama.embed(
    model="nomic-embed-text",
    input=query
)

query_embedding = response["embeddings"][0]

# -------------------------
# 7. Semantic search
# -------------------------

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# -------------------------
# 8. Display results
# -------------------------

print("\nTop Results:\n")

for i, document in enumerate(results["documents"][0]):
    print(f"{i + 1}. {document}")

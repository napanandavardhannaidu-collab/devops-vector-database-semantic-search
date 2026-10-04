import chromadb

# Create Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="devops_docs"
)

# Add DevOps documents
collection.add(
    ids=["doc1", "doc2", "doc3"],
    documents=[
        "Docker containers can be started using the docker start command.",
        "Kubernetes pods can be inspected using the kubectl get pods command.",
        "Jenkins pipelines can be used to automate CI/CD workflows."
    ],
    metadatas=[
        {"topic": "docker"},
        {"topic": "kubernetes"},
        {"topic": "jenkins"}
    ]
)

print("Documents added successfully!")
print("Total documents:", collection.count())

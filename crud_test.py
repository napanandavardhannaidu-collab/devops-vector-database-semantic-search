import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="crud_demo"
)

# CREATE
collection.add(
    ids=["doc1"],
    documents=["Docker container is running."]
)

print("1. Created document")

# READ
result = collection.get(ids=["doc1"])

print("\n2. Read document:")
print(result["documents"])

# UPDATE
collection.update(
    ids=["doc1"],
    documents=["Docker container stopped unexpectedly."]
)

print("\n3. Updated document")

# READ again
result = collection.get(ids=["doc1"])

print("Updated document:")
print(result["documents"])

# DELETE
collection.delete(ids=["doc1"])

print("\n4. Deleted document")

# Check
result = collection.get(ids=["doc1"])

print("After deletion:")
print(result["documents"])

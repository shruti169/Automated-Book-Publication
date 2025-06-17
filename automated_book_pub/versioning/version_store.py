import chromadb
from chromadb.utils import embedding_functions
from datetime import datetime
from uuid import uuid4

# Initialize ChromaDB
client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

# Optional: Use Gemini embeddings if available, otherwise use built-in
embedding_fn = embedding_functions.DefaultEmbeddingFunction()

def save_version_to_chroma(text, editor_name, notes):
    version_id = str(uuid4())
    metadata = {
        "editor": editor_name,
        "timestamp": datetime.now().isoformat(),
        "notes": notes
    }
    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[version_id]
    )
    return version_id

def get_all_versions():
    return collection.get(include=["documents", "metadatas", "ids"])

def get_version_by_id(version_id):
    results = collection.get(ids=[version_id])
    return results["documents"][0], results["metadatas"][0]

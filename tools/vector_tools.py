from crewai.tools import tool
import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./chroma_db")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
collection = client.get_or_create_collection(
    name="papers",
    embedding_function=embedding_fn
)

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

@tool("Chunk and Store")
def chunk_and_store(text: str, paper_id: str) -> str:
    """Splits text into chunks and stores them in the vector database with a paper ID."""
    chunks = chunk_text(text)
    ids = [f"{paper_id}_chunk_{i}" for i in range(len(chunks))]
    collection.add(documents=chunks, ids=ids, metadatas=[{"paper_id": paper_id}] * len(chunks))
    return f"Stored {len(chunks)} chunks for paper {paper_id}."

@tool("Retrieve Chunks")
def retrieve_chunks(query: str, n_results: int = 5) -> str:
    """Retrieves the most relevant chunks from the vector database given a query."""
    results = collection.query(query_texts=[query], n_results=n_results)
    docs = results["documents"][0]
    return "\n\n---\n\n".join(docs)
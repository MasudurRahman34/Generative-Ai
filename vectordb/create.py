from langchain_core.documents import Document
from setup import vectorStore


# single document
doc = Document(
    page_content="LangChain simplifies LLM app development",
    metadata={"source": "docs", "topic": "lanchain"},
)

ids = vectorStore.add_documents(documents=[doc])

print(ids)  # ['uuid-...',]

# Bulk add with custom IDs
docs = [
    Document(
        page_content="ChromaDB is a vector database",
        metadata={"id": "doc_1", "year": 2024},
    ),
    Document(
        page_content="LangGraph builds stateful agents",
        metadata={"id": "doc_2", "year": 2024},
    ),
]

ids = vectorStore.add_documents(documents=docs, ids=["doc1", "doc_2"])

print(ids)

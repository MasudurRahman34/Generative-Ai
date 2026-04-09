from setup import client, vectorStore
from langchain_core.documents import Document

collection = client.get_collection("my_collection")


def check_exists_by_id(id: str) -> dict | None:
    result = collection.get(ids=[id])
    if not result["ids"]:
        return None
    else:
        return result


def update_if_exist(id: str, new_text: str, new_metadata: dict) -> dict:
    existing = check_exists_by_id(id)
    if existing is None:
        return {"success": False, "message": f"Id {id} not found"}
    # collection.update(
    #     ids=[id],
    #     documents=[new_text],
    #     metadatas=[new_metadata],
    # )

    updated_document = Document(page_content=new_text, metadata=new_metadata)
    vectorStore.update_documents(ids=id, documents=[updated_document])

    updated_result = collection.get(
        ids=["doc1"], include=["embeddings", "documents", "metadatas"]
    )

    return updated_result


result = update_if_exist(
    "doc1", "ChromaDB is a vector database updated", {"id": "doc1", "year": 2027}
)

print(result)

from setup import client

collection = client.get_collection("my_collection")
# count
# print(collection.count())
# get all
list_all = collection.get()
# print(list_all)


# Fetch all documents
all_docs = collection.get(include=["documents", "metadatas"])
# print(all_docs)
# fetch by ID(s)
result = collection.get(ids=["doc1"])
# print(result)

# fetch by text

# text_result = collection.query(query_texts=["ChromaDB is a vector database"])
# print(text_result)

collections = client.list_collections()
# print([c.name for c in collections])

# Filter by metadata (where clause)
filtered = collection.get(
    where={"year": {"$eq": 2024}}, include=["documents", "metadatas", "embeddings"]
)
print(filtered)

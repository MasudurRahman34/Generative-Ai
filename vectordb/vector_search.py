from setup import vectorStore
#Search
results = vectorStore.similarity_search(query="updated", k=1)

for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")

#Use as Retriever:
retriever = vectorStore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 1,
        "fetch_k": 2,
        "landa_mult": 0.5,
    },
)
print(retriever.invoke("2027"))

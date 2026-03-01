from loader import load_txt_doccument
from splitter import split_documents
from embeddings import get_embedding_model
from vectorstore import create_vectorstore
from vectorstore import load_vectorstore
import os

if __name__ == "__main__":
    docs = load_txt_doccument("data/companyPolicies.txt")
    chunks = split_documents(docs)
    print(f"Total_chunk: {len(chunks)}\n")
    for i, chunk in enumerate(chunks[:15]):
        print(f"----chunk {i + 1}---")
        print(chunk.page_content)

    print("Loading embedding model...")
    embeddings = get_embedding_model()

    if os.path.exists("vectorestore") and os.listdir("vectorestore"):
        load_vectorstore(embeddings)
        print("vectorestore loaded")
    else:
        print("Creating vector store...")
        vectordb = create_vectorstore(chunks, embeddings)

    print("Vector store  successfully ✅")

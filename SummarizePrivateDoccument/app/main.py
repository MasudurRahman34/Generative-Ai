from loader import load_txt_doccument
from splitter import split_documents
from embeddings import get_embedding_model
from vectorstore import create_vectorstore
from vectorstore import load_vectorstore
from rag_pipeline import run_rag_query
import os

if __name__ == "__main__":
    query = "can you know about hasan?"
    result = run_rag_query(query)
    print("\n====Awnswer====")
    print(result["answer"])

    # docs = load_txt_doccument("../data/companyPolicies.txt")
    # chunks = split_documents(docs)
    # print(f"Total_chunk: {len(chunks)}\n")
    # for i, chunk in enumerate(chunks[:15]):
    #     print(f"----chunk {i + 1}---")
    #     print(chunk.page_content)

    # print("Loading embedding model...")
    # embeddings = get_embedding_model()

    # if os.path.exists("../vectorstore") and os.listdir("../vectorstore"):
    #     load_vectorstore(embeddings)
    #     print("vectorstore loaded")
    # else:
    #     print("Creating vector store...")
    #     vectordb = create_vectorstore(chunks, embeddings)

    # print("Vector store  successfully ✅")

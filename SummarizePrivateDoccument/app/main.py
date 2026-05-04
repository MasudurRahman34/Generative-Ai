from loader import load_txt_doccument
from splitter import split_documents
from embeddings import get_embedding_model
from vectorstore import create_vectorstore
from vectorstore import load_vectorstore
from rag_pipeline import run_rag_query
from pathlib import Path
import os

from rag_pipeline import build_rag_chain, run_rag_query


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "companyPolicies.txt"
VECTOR_DB_PATH = BASE_DIR / "vectordb"

if __name__ == "__main__":
    print("\n========== Legal Immigration Assistant” ==========\n")
    print("Type 'exit' to quit.\n")
    chain = build_rag_chain()
    while True:
        query = input("Enter your question: ")
        if query.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break

        try:
            result = run_rag_query(chain, query)
            print("\nLegal Assistant:")
            print(result["answer"])
        except Exception as e:
            print("\nError:")
            print(str(e))

    # query = "can you know about Eshanul kabir?"
    # result = run_rag_query(query)
    # print("\n====Awnswer====")
    # print(result["answer"])

    # docs = load_txt_doccument(DATA_PATH)
    # chunks = split_documents(docs)
    # print(f"Total_chunk: {len(chunks)}\n")
    # for i, chunk in enumerate(chunks[:15]):
    #     print(f"----chunk {i + 1}---")
    #     print(chunk.page_content)

    # print("Loading embedding model...")
    # embeddings = get_embedding_model()

    # if os.path.exists("VECTOR_DB_PATH") and os.listdir("VECTOR_DB_PATH"):
    #     load_vectorstore(embeddings)
    #     print("vectorstore loaded")
    # else:
    #     print("Creating vector store...")
    #     vectordb = create_vectorstore(chunks, embeddings)

    # print("Vector store  successfully ✅")

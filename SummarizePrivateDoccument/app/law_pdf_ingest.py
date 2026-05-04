if __name__ == "__main__":
    from loader import process_pdf_document
    from splitter import split_pdf_documents
    from embeddings import get_embedding_model
    from vectorstore import create_vectorstore
    from vectorstore import load_vectorstore
    from pathlib import Path
    import os
    import time

    BASE_DIR = Path(__file__).resolve().parent.parent

    DATA_PATH = BASE_DIR / "data" / "immigration_act_2025.pdf"
    VECTOR_DB_PATH = BASE_DIR / "vectordb"

    # query = "can you know about Eshanul kabir?"
    # result = run_rag_query(query)
    # print("\n====Awnswer====")
    # print(result["answer"])

    start_time = time.time()

    print("\n========== PDF INGESTION STARTED ==========\n")
    documents = process_pdf_document(DATA_PATH)
    print(f"Total page: {len(documents)}\n")

    chunks = split_pdf_documents(documents)
    print(f"Total_chunk: {len(chunks)}\n")

    print(chunks[0].page_content[:1000])

    print("\nMetadata:")
    print(chunks[0].metadata)

    print("\nLoading embedding model...\n")

    embeddings = get_embedding_model()

    # -----------------------------------------------------
    # 4️⃣ Create Vector Store
    # -----------------------------------------------------

    create_vectorstore(chunks, embeddings, VECTOR_DB_PATH)

    end_time = time.time()

    print("\n========== INGESTION COMPLETE ==========\n")

    print(f"Vector DB saved at: {VECTOR_DB_PATH}")

    print(f"Total processing time: {end_time - start_time:.2f} seconds")

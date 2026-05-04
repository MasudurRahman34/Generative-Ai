from langchain_community.vectorstores import FAISS


def create_vectorstore(chunks, embeddings, save_path="vectordb"):
    vectordb = FAISS.from_documents(documents=chunks, embedding=embeddings)
    vectordb.save_local(save_path)
    return vectordb


def load_vectorstore(embeddings, save_path="vectordb"):
    return FAISS.load_local(save_path, embeddings, allow_dangerous_deserialization=True)

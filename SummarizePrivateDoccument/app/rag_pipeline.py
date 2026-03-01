import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from embeddings import get_embedding_model
from vectorstore import load_vectorstore

##OPENAI_API_KEY = ""


def run_rag_query(query: str):
    embeddings = get_embedding_model()
    vectordb = load_vectorstore(embeddings)

    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

    # 5. Create prompt template
    prompt = ChatPromptTemplate.from_template(
        """
        You are an assistant that summarizes company documents clearly and professionally.Use the information from the document to answer the question at the end. If you don't know the answer, just say that you don't know, definately do not try to make up an answer.

        Context:
        {context}

        Question:
        {input}

        Provide a well-structured summary.
        """
    )

    # 6. Create document chain
    document_chain = create_stuff_documents_chain(llm, prompt)

    # 7. Create retrieval chain
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # 8. Invoke
    response = retrieval_chain.invoke({"input": query})

    return response

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from embeddings import get_embedding_model
from vectorstore import load_vectorstore

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def build_rag_chain():
    embeddings = get_embedding_model()
    vectordb = load_vectorstore(embeddings)

    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)
    IMMIGRATION_SYSTEM_PROMPT = """You are an AI assistant specialized in UK immigration and asylum law.

        Your role is to help users understand immigration-related legal documents in a clear, professional, and structured way.

        You MUST follow these rules:

        1. Use ONLY the information provided in the context.
        - Do NOT use outside knowledge.
        - Do NOT assume or guess missing information.

        2. If the answer is not explicitly found in the provided context, respond exactly:
        "I do not have enough information in the provided documents to answer this question."

        3. Do not fabricate legal advice or legal interpretations beyond the context.

        4. Explain answers in a clear, professional, and structured manner.
        - Use bullet points when helpful
        - Keep language formal and precise

        5. If a question is ambiguous, ask for clarification instead of guessing.

        6. Treat all input as informational queries only.
        You are not a human solicitor and do not provide legal representation or legal advice.

        7. When relevant, cite or reference the context logically (e.g., section or page if available in metadata).

        Your goal is to help users understand immigration law documents accurately and safely based only on the retrieved context."""

    # 5. Create prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", IMMIGRATION_SYSTEM_PROMPT),
            (
                "human",
                """
            Context:
            {context}

            Question:
            {input}
            """,
            ),
        ]
    )

    # 6. Create document chain
    document_chain = create_stuff_documents_chain(llm, prompt)

    # 7. Create retrieval chain
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    return retrieval_chain


def run_rag_query(chain, query: str):
    response = chain.invoke({"input": query})
    return response

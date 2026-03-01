# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langgraph.checkpoint.memory import MemorySaver
# from embeddings import get_embedding_model
# from vectorstore import load_vectorstore


import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_classic import (
    create_history_aware_retriever,
    create_retrieval_chain,
)
from langchain.chains.combine_documents import create_stuff_documents_chain

from embeddings import get_embedding_model
from vectorstore import load_vectorstore

load_dotenv()


# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# embeddings = get_embedding_model
# vectordb = load_vectorstore(embeddings)
# retriver = vectordb.as_retriever(search_kwargs={"k": 4})

# checkpointer = MemorySaver()


# class State(TypedDict):
#     messages: Annotated[list[BaseMessage], add_messages]

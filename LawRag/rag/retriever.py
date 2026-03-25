from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from core.config import OPENAI_API_KEY

embedding=OpenAIEmbeddings(api_key=OPENAI_API_KEY, model="text-embedding-3-large")
vectore_store=Chroma(
    collection_name="ëxample_collection",
    embedding_function=embedding,
    persist_directory="../chroma_langchain_db"
)


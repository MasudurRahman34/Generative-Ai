import chromadb
from chromadb.config import Settings
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPEN_API_KEY")
# print(OPENAI_API_KEY)


client = chromadb.PersistentClient(
    path="./chroma_db", settings=Settings(anonymized_telemetry=False)
)

# embedding Model

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=OPENAI_API_KEY)

# langchain vector chroma store

vectorStore = Chroma(
    client=client, collection_name="my_collection", embedding_function=embeddings
)
# Or create directly (auto-persists)

# vectorStore = Chroma.from_documents(
#     documents=[],
#     embedding=embeddings,
#     persist_directory="./chroma_db",
#     collection_name="my_collection",
# )

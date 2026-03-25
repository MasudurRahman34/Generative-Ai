from langchain_openai import ChatOpenAI
from core.config import OPENAI_API_KEY

llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-5-nano", temperature=0)

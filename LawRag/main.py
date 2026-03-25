from fastapi import FastAPI
from core.llm import llm

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Law Rag Running"}


@app.get("/test-llm")
async def test_llm():
    response = llm.invoke("say hellow like a friendly assistant")
    return {"response:": response.content}

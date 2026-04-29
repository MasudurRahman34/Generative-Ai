from fastapi import FastAPI
from core.llm import llm
from core.config import engine

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Law Rag Running"}


@app.get("/test-llm")
async def test_llm():
    response = llm.invoke("say hellow like a friendly assistant")
    return {"response:": response.content}


@app.get("/db-check")
async def db_check():
    # from core.db import check_db_connection
    # result = check_db_connection()
    try:
        conn = await engine.connect()
        await conn.close()
        return {"status": "success", "message": "Database is connected successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

from fastapi import FastAPI
from core.llm import llm
from contextlib import asynccontextmanager
from middlewares.cors import register_cors
from core.database import check_db_connection
from api import db_router
from api import anonymous_session_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code
    print("Starting up...")
    # database connection check
    db_status = await check_db_connection()
    print(db_status["message"])

    yield
    # shutdown code
    print("Shutting down...")


app = FastAPI(title="Law RAG API", version="1.0.0", lifespan=lifespan)

register_cors(app)

app.include_router(prefix="/api/v1/db", router=db_router.router)
app.include_router(prefix="/api/v1", router=anonymous_session_route.router)


@app.get("/")
def home():
    return {"message": "Law Rag Running"}


@app.get("/test-llm")
async def test_llm():
    response = llm.invoke("say hellow like a friendly assistant")
    return {"response:": response.content}

from fastapi import APIRouter
from services.db_service import create_database_tables

router = APIRouter()


@router.post("/create-tables")
async def db_create_tables():
    create_table = await create_database_tables()
    return {"message": "Database tables created successfully"}

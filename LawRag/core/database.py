from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from core.config import DATABASE_URL
from core.base import Base
from models.init import *
# Import all models to register them with Base

# async database engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True, pool_pre_ping=True)

# async session maker
async_session = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)


# Dependency to get DB session
async def get_db():
    async with async_session() as session:
        yield session


# Function to check database connection
async def check_db_connection():
    try:
        conn = await engine.connect()
        await conn.close()
        return {"status": "success", "message": "Database is connected successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# Function to create database tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("tables created successfully")

import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

load_dotenv()

OPENAI_API_KEY = os.getenv("OPEN_API_KEY")

# database connection

engine = create_async_engine(os.getenv("DATABASE_URL"), echo=True, future=True)

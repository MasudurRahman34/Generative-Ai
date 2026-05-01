import os

from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.getenv("OPEN_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

from core.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, BigInteger, Boolean, Text,
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone

class Message(Base):
    __tablename__ = "messages"

    id = Column(BigInteger, primary_key=True, index=True)
    conversation_id = Column(BigInteger, nullable=False, index=True)  # Foreign key to Convesation
    role = Column(String, nullable=False)  # 'user' or 'assistant'
    content = Column(Text, nullable=False)
    create_at = Column(
        TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    updated_at = (
        Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc))
    )
    deleted_at = Column(TIMESTAMP, nullable=True)
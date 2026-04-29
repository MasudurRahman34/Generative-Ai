from core.base import Base
import uuid
from sqlalchemy import Column, Integer, String, TIMESTAMP, BigInteger, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(BigInteger, primary_key=True, index=True)
    anon_session_id = Column(
        UUID(as_uuid=True), nullable=True, index=True
    )  # Foreign key to AnonymousSession.session_id
    user_id = Column(BigInteger, nullable=True, index=True)  # Foreign key to
    title = Column(String, nullable=False)

    create_at = Column(
        TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    deleted_at = Column(TIMESTAMP, nullable=True)

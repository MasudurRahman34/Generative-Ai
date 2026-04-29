import uuid
from sqlalchemy import Column, Integer, String, TIMESTAMP, BigInteger, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone
from core.base import Base


class AnonymousSession(Base):
    __tablename__ = "anonymous_sessions"

    id = Column(BigInteger, primary_key=True, index=True)
    session_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True)
    create_at = Column(
        TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    deleted_at = Column(TIMESTAMP, nullable=True)

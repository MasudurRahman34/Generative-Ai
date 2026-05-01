from core.base import Base
import uuid
from sqlalchemy import Column, Integer, String, TIMESTAMP, BigInteger, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String, index=True)
    email_verified_at = Column(TIMESTAMP, nullable=True)
    is_active = Column(Boolean, default=True)
    create_at = Column(
        TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    deleted_at = Column(TIMESTAMP, nullable=True)

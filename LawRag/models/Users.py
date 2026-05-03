# models/user.py

from datetime import datetime, timezone

from sqlalchemy import String, TIMESTAMP, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)

    email: Mapped[str] = mapped_column(String, unique=True, index=True)

    password: Mapped[str] = mapped_column(String)

    name: Mapped[str] = mapped_column(String, index=True)

    email_verified_at: Mapped[datetime | None] = mapped_column(TIMESTAMP, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    create_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    deleted_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )

    # Relationships
    conversations: Mapped[list["Conversation"]] = relationship(back_populates="user")

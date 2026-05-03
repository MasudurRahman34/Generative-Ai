from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class AnonymousSessionBase(BaseModel):
    pass


class AnonymousSessionCreate(AnonymousSessionBase):
    pass


class AnonymousSessionResponse(AnonymousSessionBase):
    id: int
    session_id: UUID
    create_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

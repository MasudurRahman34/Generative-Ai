from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services.anonymous_session_service import AnonymousSessionService
from schemas.anonymous_session_schema import (
    AnonymousSessionCreate,
    AnonymousSessionResponse,
)
from core.database import get_db

router = APIRouter(
    prefix="/anonymous-sessions",
    tags=["Anonymous Sessions"],
)


@router.post("/", response_model=AnonymousSessionResponse)
async def create_anonymous_session(
    session_data: AnonymousSessionCreate, db: AsyncSession = Depends(get_db)
):
    service = AnonymousSessionService(db)
    try:
        new_session = await service.create_anonymous_session(session_data)
        return new_session
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{session_id}", response_model=AnonymousSessionResponse)
async def get_anonymous_session(session_id: UUID, db: AsyncSession = Depends(get_db)):
    service = AnonymousSessionService(db)
    session = await service.get_anonymous_session_by_session_id(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

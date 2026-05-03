from uuid import UUID
from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.AnonymousSessions import AnonymousSession
from schemas.anonymous_session_schema import AnonymousSessionCreate


class AnonymousSessionService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_anonymous_session(
        self, session_data: AnonymousSessionCreate
    ) -> AnonymousSession:
        try:
            new_session = AnonymousSession()
            self.db_session.add(new_session)
            await self.db_session.commit()
            await self.db_session.refresh(new_session)
            return new_session
        except Exception as e:
            await self.db_session.rollback()
            raise e

    async def get_anonymous_session_by_session_id(
        self, session_id: UUID
    ) -> AnonymousSession | None:
        result = await self.db_session.execute(
            select(AnonymousSession).where(AnonymousSession.session_id == session_id)
        )
        return result.scalars().first()

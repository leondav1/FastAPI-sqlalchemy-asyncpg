import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from app_isberg.models.models import Base

dotenv_path = Path('.')/'.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

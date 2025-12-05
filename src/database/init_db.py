# Database initialization
from .session import engine, Base
from src.core.config import settings
import asyncpg

async def ensure_database():
    conn = await asyncpg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASS,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
    )
    db_exists = await conn.fetchval(f"SELECT 1 FROM pg_database WHERE datname='{settings.DB_NAME}'")
    if not db_exists:
        await conn.execute(f'CREATE DATABASE {settings.DB_NAME}')
    await conn.close()

async def init_models():
    # Tables create karne ke liye
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

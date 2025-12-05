from fastapi import FastAPI
from src.database.init_db import ensure_database, init_models
from src.api.v1 import users
from src.database.session import Base, engine, test_db_connection
import asyncio

app = FastAPI(title="Secure Users CRUD App")
app.include_router(users.router)

@app.on_event("startup")
async def startup_event():
    # 1️⃣ Ensure database exists (dev mode)
    await ensure_database()
    
    # 2️⃣ Create tables if not exist
    await init_models()

    # 3️⃣ Optional: Test DB connection
    print("Database and tables ready!")
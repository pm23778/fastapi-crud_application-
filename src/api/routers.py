# API routers configuration
from fastapi import APIRouter
from src.api.v1 import users

api_router = APIRouter()

# Include all version 1 routes
api_router.include_router(users.router, prefix="/api/v1", tags=["Users"])

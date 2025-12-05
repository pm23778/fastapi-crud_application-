# User Pydantic schemas
from pydantic import BaseModel, EmailStr
from pydantic_settings import SettingsConfigDict

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = SettingsConfigDict(
        from_attributes = True   # orm_mode ka new name
    )

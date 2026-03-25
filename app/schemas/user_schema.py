from pydantic import BaseModel, EmailStr, Field
from uuid import UUID


class UserBase(BaseModel):
    email: EmailStr
    role: str = "student"

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=72, description="Password must be between 8 and 72 characters")

class UserResponse(UserBase):
    id: UUID
    is_active: bool

    # the reason we need this config is because SQLAlchemy models don't return dicts, they return objects with attributes. This tells Pydantic to read data from attributes instead of expecting a dict.
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
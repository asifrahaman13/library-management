from sqlmodel import Field
from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel


# Pydantic model for the user authentication fields.
class User(BaseModel):
    user_id: str | None = None
    username: str | None = None


class UserBase(BaseModel):
    username: str
    password: str


class UserDetails(BaseModel):
    user_id: str | None = None
    username: str | None = None


# Create a UserDatabase class that inherits from SQLModel
class UserDatabase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str

    __config__ = {"orm_mode": True}

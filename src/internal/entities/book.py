from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field


class BookBase(BaseModel):
    Title: str
    User: str | None = None
    Authors: str
    Publication_Date: Optional[str] = None
    ISBN: str
    Description: Optional[str] = None


class BookDatabase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    User: str
    Title: str
    Authors: str 
    Publication_Date: Optional[str] = None
    ISBN: str = Field(index=False, sa_column_kwargs={"unique": True})
    Description: Optional[str] = None


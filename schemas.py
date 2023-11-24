from typing import Optional
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

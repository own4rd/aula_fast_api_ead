from typing import Optional
from pydantic import BaseModel

class PostBaseSchema(BaseModel):
    title: str

class PostCreateSchema(PostBaseSchema):
    pass

class PostSchema(PostBaseSchema):
    id: Optional[int] = None

    class Config:
        orm_mode = True

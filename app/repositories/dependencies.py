from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.repositories.post import PostRepository


def get_post_repository(db: Session = Depends(get_db)):
    return PostRepository(
        db=db
    )

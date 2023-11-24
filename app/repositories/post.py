from sqlalchemy.orm import Session
from app.database.models import Post

class PostRepository:
    __slots__ = ["db"]

    def __init__(self, db: Session) -> None:
        self.db = db
    
    def create(self, post: Post):
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
        return post
    
    def find_all(self):
        return self.db.query(Post).all()

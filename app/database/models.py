from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=True)
    title = Column(String)

from fastapi import FastAPI, HTTPException, status, Depends
import models, schemas, crud
from database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get('/posts/', response_model=list[schemas.Post])
async def get_posts(db: Session = Depends(get_db)):
    posts = crud.get_posts(db) 
    return posts  


@app.post('/posts/', response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.create_post(db, post)
    return db_post

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)

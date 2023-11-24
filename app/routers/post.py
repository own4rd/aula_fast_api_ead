from fastapi import APIRouter, status, Depends
from app.schemas.post import PostSchema, PostCreateSchema
from app.database.models import Post
from app.services.post import PostService
from app.services.dependencies import get_post_service

router = APIRouter()

@router.get('/posts/', response_model=list[PostSchema], status_code=status.HTTP_200_OK)
async def get_posts(post_service: PostService = Depends(get_post_service)):
    posts = post_service.find_all()
    return posts  



@router.post('/posts/', response_model=PostSchema, status_code=status.HTTP_201_CREATED)
async def create_post(request: PostCreateSchema, post_service: PostService = Depends(get_post_service)):
    post = post_service.create(Post(**request.model_dump()))
    return post


from fastapi import Depends

from app.services.post import PostService
from app.repositories.post import PostRepository
from app.repositories.dependencies import get_post_repository

def get_post_service(post_repository: PostRepository = Depends(get_post_repository)):
    return PostService(
        repository=post_repository
    )

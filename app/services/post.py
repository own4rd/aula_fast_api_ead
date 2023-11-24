from app.database.models import Post

class PostService:
    __slots__ = ["repository"]

    def __init__(self, repository) -> None:
        self.repository = repository

    def create(self, post: Post):
        return self.repository.create(post)

    def find_all(self):
        return self.repository.find_all()

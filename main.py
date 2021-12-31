from fastapi import FastAPI

from db import models
from db.database import engine
from router import blog_get, blog_post, user

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return {'message': 'Hello World'}


models.Base.metadata.create_all(engine)
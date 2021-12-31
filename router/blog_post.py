from typing import Optional

from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog'],
)


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'data': blog,
        'id': id,
        'version': version,
    }


@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel,
                   id: int,
                   comment_id: int = Query(None,
                                           title='id of the comment',
                                           description='Description of comment',
                                           alias='commentId',
                                           deprecated=True,
                                           )
                   ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
    }
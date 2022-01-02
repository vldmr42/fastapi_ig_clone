from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from sqlalchemy.orm import Session

from db.database import get_db

from typing import List, Optional

router = APIRouter(
    prefix='/product',
    tags=['product'],
)

products = ['watch', 'camera', 'phone']


@router.get('/all')
def get_all_products():
    data = ' '.join(products)
    return Response(content=data, media_type='text/plain')


@router.get('/withheader')
def get_product(
        response: Response,
        custom_header: Optional[List[str]] = Header(None)
):
    response.headers['custom_response_header'] = ' '.join(custom_header)
    return products

@router.get('/{id}', responses={
    200: {
        'content': {
            'text/html': {
                'example': "<div>Product</div>"}
        },
        'description': "Returns the HTML for an object"
    },
    404: {
        'content': {
            'text/plain': {'example': 'Product not available'}
        },
        'description': "A clear text error message"
    },
})
def get_product(id: int):
    if id > len(products):
        out = 'Product not available'
        return PlainTextResponse(status_code=404, content=out, media_type='text/plain')
    else:
        product = products[id]
        out = f"""
        <head></head>
        <div>{product}</div>
        """
        return HTMLResponse(
            content=out, media_type='text/html',
        )

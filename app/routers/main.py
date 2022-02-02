from fastapi import APIRouter, Request

router = APIRouter()


@router.get('/')
def index(request: Request):
    return {
        'message': 'Hello world',
        'status': 'OK',
    }

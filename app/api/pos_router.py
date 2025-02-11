from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_pos():
    return {'status': 'pos is running'}
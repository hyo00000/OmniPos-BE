from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_kiosk():
    return {'status': 'kiosk is running'}
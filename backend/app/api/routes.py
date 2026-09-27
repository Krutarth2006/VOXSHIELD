from fastapi import APIRouter

router = APIRouter(prefix='/api', tags=['voxshield'])


@router.get('/health')
def health():
    return {'status': 'ok', 'service': 'VOXSHIELD'}

from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
async def webhook():
    return 'OK'

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def root():
    return {"message": "Hello World"}

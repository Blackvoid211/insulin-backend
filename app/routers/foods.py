from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_foods():
    return {"message": "Foods endpoint working!"}


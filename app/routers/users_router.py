from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)


@router.get("/")
async def test_users():
    return {"message": "It Worked!"}

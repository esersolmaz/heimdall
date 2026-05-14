from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(payload: dict):
    return {"access_token": "demo-token", "token_type": "bearer", "user": payload.get("username", "analyst")}

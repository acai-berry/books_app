from fastapi import APIRouter


api_router = APIRouter()


@api_router.get("/health", tags=["health-check"])
async def health():
    return {"health": "It's working ✨"}

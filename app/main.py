from fastapi import FastAPI

from app.database import database
from app.routers import books_router, health_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    database.connect()


@app.on_event("shutdown")
async def shutdown():
    database.disconnect()


app.include_router(books_router.api_router)
app.include_router(health_router.api_router)

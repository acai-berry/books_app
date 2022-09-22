from fastapi import FastAPI

from database import database
from routers import books_router, health_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(books_router.api_router)
app.include_router(health_router.api_router)

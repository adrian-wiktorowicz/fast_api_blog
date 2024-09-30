from fastapi import FastAPI
from core.config import settings


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_NAME)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

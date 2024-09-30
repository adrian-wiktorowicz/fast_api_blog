from fastapi import FastAPI
from backend.core.config import settings

from backend.db.session import engine
from backend.db.base_class import Base


def create_tables():
    Base.metadata.create_all(bind=engine)

def start_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_NAME)
    create_tables()
    return app

app = start_app()


@app.get("/")
async def home():
    return {'msg':'H3H3'}

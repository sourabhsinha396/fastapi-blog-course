from fastapi import FastAPI
from core.config import settings
from apis.base import api_router
from apps.base import app_router


def include_router(app):
    app.include_router(api_router)
    app.include_router(app_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
    include_router(app)
    return app 


app = start_application()

from fastapi import FastAPI
from core.config import settings


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
    return app 


app = start_application()


@app.get("/")
def hello():
    return {"msg":"Hello FastAPI 🚀"}
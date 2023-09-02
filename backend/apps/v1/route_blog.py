from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def home(request: Request):
    print(dir(request))
    return templates.TemplateResponse("blogs/home.html", {"request": request})
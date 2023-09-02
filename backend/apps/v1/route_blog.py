from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session 
from db.repository.blog import list_blogs
from db.session import get_db


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    context = {"request": request,"blogs":blogs}
    return templates.TemplateResponse("blogs/home.html", context=context)
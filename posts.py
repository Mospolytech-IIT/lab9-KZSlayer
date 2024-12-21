from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.requests import Request
import crud
import schemas
import database
import os
router = APIRouter()

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

@router.get("/create", response_class=HTMLResponse)
def create_post_form(request: Request):
    """Страница для создания нового поста."""
    return templates.TemplateResponse("create_post.html", {"request": request})

@router.post("/create", response_class=RedirectResponse)
def create_post(title: str = Form(...), content: str = Form(...), user_id: int = Form(...), db: Session = Depends(database.get_db)):
    """Функция для создания нового поста."""
    post = schemas.PostCreate(title=title, content=content, user_id=user_id)
    crud.create_post(db, post)
    return RedirectResponse(url="/posts/", status_code=303)

@router.get("/", response_class=HTMLResponse)
def list_posts(request: Request, db: Session = Depends(database.get_db)):
    """Страница для отображения всех постов."""
    posts = crud.get_posts(db)
    return templates.TemplateResponse("list_posts.html", {"request": request, "posts": posts})

@router.get("/edit/{post_id}", response_class=HTMLResponse)
def edit_post_form(request: Request, post_id: int, db: Session = Depends(database.get_db)):
    """Страница для редактирования поста."""
    post = crud.get_post_by_id(db, post_id)
    return templates.TemplateResponse("edit_post.html", {"request": request, "post": post})

@router.post("/edit/{post_id}", response_class=RedirectResponse)
def edit_post(post_id: int, title: str = Form(...), content: str = Form(...), db: Session = Depends(database.get_db)):
    """Функция для обновления поста."""
    post = schemas.PostCreate(title=title, content=content)
    crud.update_post_content(db, post_id, post)
    return RedirectResponse(url="/posts/", status_code=303)

@router.get("/delete/{post_id}", response_class=RedirectResponse)
def delete_post(post_id: int, db: Session = Depends(database.get_db)):
    """Функция для удаления поста."""
    crud.delete_post(db, post_id)
    return RedirectResponse(url="/posts/", status_code=303)

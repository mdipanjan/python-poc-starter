# src/api/routes/base.py
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from src.core.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="src/frontend/templates")

@router.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "settings": settings}
    )
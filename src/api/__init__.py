# src/api/__init__.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.core.config import settings
from .routes.base import router as base_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Make sure the directories exist before mounting
app.mount("/static", StaticFiles(directory="src/frontend/templates"), name="static")
templates = Jinja2Templates(directory="src/frontend/templates")

# Include the base router
app.include_router(base_router)
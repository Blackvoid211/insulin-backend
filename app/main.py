# app/main.py
from dotenv import load_dotenv
load_dotenv()  # ensure .env values are available early

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import engine
from app import models
from app.routers import foods 
from app.models import Base
from app.auth import router as auth_router

app = FastAPI(title="Insulin Backend - Minimal")

app.include_router(foods.router, prefix="/foods", tags=["foods"])
# Create tables on startup (development convenience)
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# CORS configured from environment
origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origins if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router, prefix="/auth", tags=["auth"])


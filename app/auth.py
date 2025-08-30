# app/auth.py
from dotenv import load_dotenv
load_dotenv()  # ensure .env is loaded if not already

import os
from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import User
from app.schemas import RegisterSchema, LoginSchema

router = APIRouter()
pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGO = "HS256"

def get_jwt_secret():
    # read secret at runtime from environment (safer if .env changes)
    return os.getenv("JWT_SECRET", "devsecret")

@router.post("/register")
def register(payload: RegisterSchema, db: Session = Depends(get_db)):
    # check existing
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = pwd_ctx.hash(payload.password)
    user = User(email=payload.email, hashed_password=hashed, name=payload.name)
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"id": user.id, "email": user.email, "name": user.name}

@router.post("/login")
def login(payload: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not pwd_ctx.verify(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    SECRET = get_jwt_secret()
    token = jwt.encode({"sub": user.email}, SECRET, algorithm=ALGO)
    return {"access_token": token, "token_type": "bearer"}

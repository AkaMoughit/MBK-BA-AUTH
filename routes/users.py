# routes/users.py
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.users import User, UserBase

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/")
async def login_user(user_email: str,user_password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email, User.password_hash == user_password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user.username
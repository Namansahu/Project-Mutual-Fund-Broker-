from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import User, Portfolio
from app.services.rapidapi_integration import fetch_fund_data
from app.database import get_db
from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Request models
class UserRequest(BaseModel):
    email: str
    password: str

class FundRequest(BaseModel):
    family: str

# User Registration
@router.post("/register")
def create_account(user: UserRequest, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    new_user = User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "Account created successfully"}

# User Login
@router.post("/login")
def login(user: UserRequest, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

# Fetch Funds
@router.post("/funds")
def get_funds(fund_request: FundRequest, db: Session = Depends(get_db)):
    funds = fetch_fund_data(fund_request.family)
    if not funds:
        raise HTTPException(status_code=404, detail="No funds found")
    return funds

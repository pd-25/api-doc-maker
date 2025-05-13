from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from database.session import get_db
from sqlalchemy.orm import Session
from repository.auth.auth import *
from config.hashing import Hasher


router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Authenticate user and return access token.
    """
    # Here you would typically verify the username and password
    # For demonstration, we will just return a dummy token
    user = authenticate_user(db, form_data.username, form_data.password)
    if user and Hasher.verifyPassword(form_data.password, user.password):
       return user
    return False
        
    
    
def authenticate_user(db: Session, email: str, password: str):
    findUser = getUserByUsername(db, email, password)
    if findUser and Hasher.verifyPassword(password, findUser.password):
        return findUser
    return False
    
    
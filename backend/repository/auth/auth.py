from sqlalchemy.orm import Session
from models.user import User

def getUserByUsername(email: str, db: Session):
    user = db.query(User).filter(User.email==email).first()
    return user
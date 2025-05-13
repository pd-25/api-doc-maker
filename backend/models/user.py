from database.base_class import Base
from sqlalchemy import Column, Integer, String
class User(Base):
    id= Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    position = Column(String(50), nullable=False)
    
    
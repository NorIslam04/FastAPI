from sqlalchemy import Column, Integer, String
from db import Base

class User(Base):
    __tablename__ = "usr"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

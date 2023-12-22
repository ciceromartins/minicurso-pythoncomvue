from sqlalchemy import Column, Integer, String, Boolean
from . import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    phoneNumber = Column(String(15))
    email = Column(String(60))
    isAdmin = Column(Boolean, default=False)
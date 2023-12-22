from fastapi import APIRouter
from contexts.database import dbContext
from models.usersModel import Users

usersRoute = APIRouter()

@usersRoute.get("/")
def getAll():
    users = dbContext.query(Users).all()
    return users
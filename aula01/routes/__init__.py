from fastapi import APIRouter
from .usersRoute import usersRoute
router = APIRouter()

router.include_router(usersRoute, prefix="/users")
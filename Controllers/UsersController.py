from fastapi import APIRouter
from Dtos.User.UserSignInDto import UserSignInDto
from Services.UsersService import UsersService
from Dtos.User.UserDto import UserDto
router = APIRouter()
service = UsersService()

@router.get("/getAllUsers")
def getAllUsers():
    return service.getAllUsers()

@router.post("/signIn")
def signIn(user:UserSignInDto):
    return service.signIn(user)

@router.post("/register")
def register(user:UserDto):
    return service.register(user)
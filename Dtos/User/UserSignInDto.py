from pydantic import BaseModel

class UserSignInDto(BaseModel):
    email:str
    password:str
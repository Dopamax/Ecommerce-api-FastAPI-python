from pydantic import BaseModel

class UserDto(BaseModel):
    id:int
    name:str
    tel:str
    email:str
    password:str
    city:str
    country:str
from pydantic import BaseModel

class ItemUserDto(BaseModel):
    name:str
    tel:str
    email:str
    city:str
    country:str
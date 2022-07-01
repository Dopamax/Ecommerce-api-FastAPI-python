from pydantic import BaseModel

class ProductDto(BaseModel):
    id:int
    designation:str
    price:float
    catalogId:int
from pydantic import BaseModel

class CatalogDto(BaseModel):
    id:int
    designation:str
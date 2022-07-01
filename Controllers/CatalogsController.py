from fastapi import APIRouter
#from Models.Catalog import Catalog
from Dtos.Catalog.CatalogDto import CatalogDto
from Services.CatalogsService import CatalogsService

router = APIRouter()
service = CatalogsService()

@router.get("/getAllCatalogs")
async def getAllCatalogs():
    return service.getAllCatalogs()

@router.post("/add")
async def addCatalog(catalog:CatalogDto):
    return service.addCatalog(catalog)
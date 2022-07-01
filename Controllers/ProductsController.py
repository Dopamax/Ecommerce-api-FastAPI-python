from fastapi import APIRouter
from Services.ProductsService import ProductsService
from Dtos.Product.ProductDto import ProductDto
router = APIRouter()
service = ProductsService()

@router.get("/getAllProducts")
def getAllProducts():
    return service.getAllProducts()

@router.post("/add")
def addProduct(product:ProductDto):
    service.addProduct(product)
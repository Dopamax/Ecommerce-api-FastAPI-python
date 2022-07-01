from Controllers import CatalogsController,ProductsController,UsersController
from fastapi import FastAPI

app = FastAPI()
#api_router = APIRouter()

app.include_router(CatalogsController.router, prefix="/Catalogs", tags=["Catalogs"])
app.include_router(ProductsController.router, prefix="/Products", tags=["Products"])
app.include_router(UsersController.router, prefix="/Users", tags=["Users"])
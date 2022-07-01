from Models.Catalog import Catalog

class CatalogsService:

    liste = []
    liste.append(Catalog(1,"TV"))
    liste.append(Catalog(2,"Laptops"))
    liste.append(Catalog(3,"Smartphones"))

    def __init__(self):
        self
        
    def getAllCatalogs(self):
        return (self.liste)

    def addCatalog(self,catalog:Catalog(0,"")):
        self.liste.append(catalog)
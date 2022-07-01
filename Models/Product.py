class Product:
    id:int
    designation:str
    price:float
    catalogId:int

    def __init__(self, id, designation, price, catalogId):
        self.id = id
        self.designation = designation
        self.price = price
        self.catalogId = catalogId
from Models.Product import Product

class ProductsService:
    products = []
    products.append(Product(1,"Samsung 23",360,1))
    products.append(Product(2,"LG 60",560,1))
    products.append(Product(3,"Dell XS",260,2))
    products.append(Product(4,"HP RV-511",500,2))
    products.append(Product(5,"Apple 11",360,3))
    products.append(Product(6,"Xaomi Redmi 9",360,3))
    
    def getAllProducts(self):
        return self.products

    def addProduct(self, product:Product):
        self.products.append(product)
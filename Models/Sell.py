from numpy import number
import Product
import User

class Sell:
    def __init__(self, product: Product, quantity:int, user:User):
        self.product = product
        self.quantity = quantity
        self.user = user
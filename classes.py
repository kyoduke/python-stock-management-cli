class Product:
    
    def __init__(self, name, price: int, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def add_to_stock(self, quantity):
        self.stock += quantity

    def remove_from_stock(self, quantity):
        self.stock -= quantity       
     
    def __str__(self) -> str:
        return f'{self.name} | R$ {self.price} | {self.stock}'

class ProductStockManagement:

    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_all_products(self):
        return self.products

    def find_and_add_quantity(self, product_name: str, quantity: int):
        for product in self.products:
            if product.name == product_name:
                product.stock += quantity

    def find_and_remove_quantity(self, product_name: str, quantity: int):
        for product in self.products:
            if product.name == product_name:
                product.stock = product.stock - quantity   

    def remove_product(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    




from product import Product
"""
____________________________________
OrderLine                           |   <-- Class Name
____________________________________|   
- __product: Product                |   <-- Attributes
- __quanity: int                    |
____________________________________|
+ calculate_subtotal: float         |   <-- Methods
+ get_product(): Product            |
+ display_information(): None       |
___________________________________ |
"""
class OrderLine:
    def __init__(self, product: Product, quantity: int):
        # Association: OrderLine refers to a Product but does not own it
        self.__product: Product = product
        self.__quantity: int = quantity
 
    def get_product(self) -> Product:
        return self.__product
 
    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity
 
    def display_information(self) -> None:
        print(f"{self.__product.get_name()} x {self.__quantity} "
              f"= ${self.calculate_subtotal():.2f}")
 
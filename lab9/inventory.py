from product import Product
"""
inventory.add_product(product1) # pass the product to inventory class to store in a list
^ Hints to use list
_____________________________________
Inventory                            |   <-- Class Name
_____________________________________|   
- __products: list[Products]         |   <-- Attributes
_____________________________________|
+ add_product(product: Product)      |   <-- Methods
+ search_product(product_id: str)    |
+ display_all()                      |
+ to_list(): list[dict]              |
_____________________________________|
"""
class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product):
        self.__products.append(product)

    def search_product(self, product_id: str):
        for product in self.__products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return
        
        for product in self.__products:
            product.display_information()
            print("-" * 20)

    def to_list(self):
        # Converts every Product into a dictionary for saving.
        return [product.to_dict() for product in self.__products]
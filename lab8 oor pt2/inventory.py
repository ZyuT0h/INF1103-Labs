from product import Product
"""
________________________________________________
Inventory                                       |   <-- Class Name
________________________________________________|   
- __products: list[Product]                     |   <-- Attributes
________________________________________________|
+ get_products(): list [Product]                |
+ add_product(product: Product): None           |   <-- Methods
+ find_product(product_id: str): Product|None   |
+ remove_product(product_id: str): None         |
+ to_list(): list[dict]                         |
+ display_all(): None                           |
________________________________________________|
"""
class Inventory:
    def __init__(self):
        self.__products: list[Product]= []

    def get_products(self) -> list[Product]:
        # Return a copy so outside code can't modify the internal list
        return list(self.__products)
    
    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product is None:
            print("Product not found.")
            return
        # Only reference is removed; Product object itself still exists
        self.__products.remove(product)
    
    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def display_all(self) -> None:
        if not self.__products:
            print("Inventory is empty.")
            return
 
        for product in self.__products:
            product.display_information()
            print(product.get_fulfilment_info())
            print("-" * 20)

    def to_list(self) -> list[dict]:
        # Converts every Product into a dictionary for saving.
        return [product.to_dict() for product in self.__products]
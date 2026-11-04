from product import Product
from canbeshipped import CanBeShipped
"""
_____________________________________
PhysicalProduct                      |   <-- Class Name
_____________________________________|   
- __weight                           |   <-- Attributes
_____________________________________|
+ display_information(): void        |   <-- Methods
+ get_fulfilment_info(): str         |
+ calculate_shipping_cost(): float   |
_____________________________________|
"""
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight 

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 2
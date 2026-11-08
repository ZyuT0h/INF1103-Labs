from product import Product
from supplier import Supplier
from canbeshipped import CanBeShipped
"""
_____________________________________
PhysicalProduct                      |   <-- Class Name
_____________________________________|   
- __weight: float                    |   <-- Attributes
_____________________________________|
+ display_information(): None        |   <-- Methods
+ to_dict: dict                      |
+ get_fulfilment_info(): str         |
+ calculate_shipping_cost(): float   |
_____________________________________|
"""
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight 

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 2
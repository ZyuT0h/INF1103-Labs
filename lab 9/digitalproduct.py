from product import Product
from supplier import Supplier
"""
_____________________________________
DigitalProduct                       |   <-- Class Name
_____________________________________|   
- __download_size: float             |   <-- Attributes
_____________________________________|
+ get_fulfilment_info(): str         |
+ to_dict(): dict                    |
+ display_information(): None        |   <-- Methods
_____________________________________|
"""
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self)-> None:
        super().display_information()
        print(f"Download size: {self.__download_size} mb")

    def to_dict(self)-> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    def get_fulfilment_info(self)-> str:
        return "This product is delivered digitally via download."
from product import Product

"""
_____________________________________
DigitalProduct                       |   <-- Class Name
_____________________________________|   
- __download_size                    |   <-- Attributes
_____________________________________|
+ display_information(): void        |   <-- Methods
+ get_fulfilment_info(): str         |
_____________________________________|
"""
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download size: {self.__download_size} mb")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    def get_fulfilment_info(self):
        return "This product is delivered digitally via download."
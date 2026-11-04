from product import Product

"""
_____________________________________
DigitalProduct                       |   <-- Class Name
_____________________________________|   
- __download_size                    |   <-- Attributes
_____________________________________|
+ display_information()              |   <-- Methods
_____________________________________|
"""
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download size: {self.__download_size} mb")

    def get_fulfilment_info(self):
        return "This product is delivered digitally via download."
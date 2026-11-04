from abc import ABC, abstractmethod
"""
_____________________________________
<<abstract>>                         |
Product                              |   <-- Class Name
_____________________________________|
- __product_id: String               |    
- __name: String                     |   <-- Attributes
- __price: float                     |
- __stock: int                       |
_____________________________________|
+ get_product_id(): void             |
+ update_stock(quantity : int): void |   <-- Methods
+ display_information(): void        |
+ to_dict(): dict                    |
+ get_fulfilment_info()              |
_____________________________________|
"""
# ABC makes Product an abstract base class
class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity: int):
        if self.__stock + quantity < 0:
            print("Not enough stock!")
            return
        self.__stock += quantity

    def display_information(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

    def to_dict(self):
        """Converts this product into a dictionary so it can be saved as JSON.
        Keys match the old file format, so an existing inventory.json still loads. """ 
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}

    # @abstractmethod forces subclasses to implement the method.
    @abstractmethod
    def get_fulfilment_info(self):
        pass
from abc import ABC, abstractmethod
from supplier import Supplier
"""
_____________________________________
<<abstract>>                         |
Product                              |   <-- Class Name
_____________________________________|
- __product_id: str                  |    
- __name: str                        |   <-- Attributes
- __price: float                     |
- __stock: int                       |
- __supplier: Supplier               |
_____________________________________|
+ get_product_id(): str              |
+ get_fulfilment_info() (abstract)   |   <-- Methods
+ get_name(): str                    |
+ get_price(): float                 |
+ get_supplier(): Supplier           |
+ update_stock(quantity : int): None |
+ to_dict(): dict                    |
+ display_information(): None        |
_____________________________________|
"""
# ABC makes Product an abstract base class
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier: Supplier = supplier
    
    def get_product_id(self) -> str:
        return self.__product_id
 
    def get_name(self) -> str:
        return self.__name
 
    def get_price(self) -> float:
        return self.__price
 
    def get_supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity: int) -> None:
        if self.__stock + quantity < 0:
            print("Not enough stock!")
            return
        self.__stock += quantity

    def display_information(self) -> None:
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        print(f"Supplier: {self.__supplier.get_name()}")


    def to_dict(self) -> dict:
        """Converts this product into a dictionary so it can be saved as JSON."""
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock,
                "supplier": self.__supplier.to_dict()}

    # @abstractmethod forces subclasses to implement the method.
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
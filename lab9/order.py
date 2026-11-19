from product import Product
from orderline import OrderLine
from discount import DiscountStrategy, NoDiscount

"""
_________________________________________________________
Order                                                    |   <-- Class Name
_________________________________________________________|   
- __order_id: str                                        |   <-- Attributes
- __order_lines: list(OrderLine)                         |
- __discount: DiscountStrategy                           |
_________________________________________________________|
+ add_order_line(product: Product, quantity: int): None  |   <-- Methods
+ remove_order_line(product_id: str): None               |
+ set_discount(discount: DiscountStrategy): None         |
+ calculate_total: float                                 |
+ display_order(): None                                  |
_________________________________________________________|
"""
class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None):
        self.__order_id: str = order_id
        # Composition: Order creates and owns its OrderLines
        self.__order_lines: list[OrderLine] = []
        # Association: Order uses a strategy but does not own it
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount
    
    def add_order_line(self, product: Product, quantity: int) -> None:
        # The OrderLine is created HERE, inside the Order - never passed in
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)
 
    def remove_order_line(self, product_id: str) -> None:
        for line in self.__order_lines:
            if line.get_product().get_product_id().upper() == product_id.upper():
                self.__order_lines.remove(line)
                return
        print("Order line not found.")
 
    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.__discount.apply(total)
    
    def display_order(self) -> None:
        print(f"Order {self.__order_id}")
        if not self.__order_lines:
            print("  (no items)")
        for line in self.__order_lines:
            print("  ", end="")
            line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")
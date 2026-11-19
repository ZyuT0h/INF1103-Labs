from abc import ABC, abstractmethod
"""
______________________________________________
<<abstract>>                                  |
CanBeShipped                                  |   <-- Class Name
______________________________________________|
+ calculate_shipping_cost(): float (abstract) |   <-- Methods
______________________________________________|
"""
class CanBeShipped(ABC):

    # @abstractmethod forces subclasses to implement the method.
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass
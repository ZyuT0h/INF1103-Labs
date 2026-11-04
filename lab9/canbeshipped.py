from abc import ABC, abstractmethod

class CanBeShipped(ABC):

    # @abstractmethod forces subclasses to implement the method.
    @abstractmethod
    def calculate_shipping_cost(self):
        pass
from abc import ABC, abstractmethod
"""
____________________________________________
<<abstract>>                                |
DiscountStrategy                            |   <-- Class Name
____________________________________________|
+ apply(total: float): float (abstract)     |   <-- Methods
____________________________________________|
Subclasses: NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount
"""
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.__percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.__percentage / 100)


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float):
        self.__threshold = threshold
        self.__amount = amount

    def apply(self, total: float) -> float:
        return total - self.__amount if total >= self.__threshold else total


class StudentDiscount(DiscountStrategy):
    """Fourth strategy: flat 5% off. """
    def apply(self, total: float) -> float:
        return total * 0.95
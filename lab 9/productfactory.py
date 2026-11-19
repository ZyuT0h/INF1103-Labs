from product import Product
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from supplier import Supplier
"""
_________________________________________________
ProductFactory                                   |   <-- Class Name
_________________________________________________|
(no attributes)                                  |
_________________________________________________|
+ create(product_type, product_id, name, price,  |   <-- Method (static)
         stock, supplier, extra): Product        |
_________________________________________________|
"""
class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock: int, supplier: Supplier, extra: float = 0.0) -> Product:
        """extra = weight (kg) for physical, download size (MB) for digital."""
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock, supplier, extra)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock, supplier, extra)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
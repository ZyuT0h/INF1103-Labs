"""Lab 8 tests - run with: python lab8_tests.py
Each section matches a section of the lab sheet."""
from supplier import Supplier
from product import Product
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from inventory import Inventory
from order import Order


def show_product_details(product: Product) -> None:
    """Section 6.2 - works for ANY Product subclass without changes (LSP)."""
    product.display_information()
    print(product.get_fulfilment_info())


def test_association() -> None:
    print("\n===== 2. ASSOCIATION: Supplier - Product =====")
    supplier = Supplier("S001", "TechWorld Pte Ltd", "sales@techworld.sg")
    laptop = PhysicalProduct("P001", "Laptop", 1299.90, 10, supplier, 1.8)
    ebook = DigitalProduct("D001", "Python eBook", 19.90, 100, supplier, 25.5)

    print("Supplier info through the laptop:")
    laptop.get_supplier().display_information()
    print("\nSupplier info through the ebook:")
    ebook.get_supplier().display_information()

    print("\nSame supplier object?", laptop.get_supplier() is ebook.get_supplier())
    print("Supplier is a separate object from product?", laptop.get_supplier() is not laptop)

    # Predict first: what happens after del supplier?
    del supplier
    print("\nAfter 'del supplier', laptop can still reach it:")
    laptop.get_supplier().display_information()


def test_aggregation() -> None:
    print("\n===== 3. AGGREGATION: Inventory - Product =====")
    supplier = Supplier("S002", "PaperCo", "hello@paperco.sg")
    # Product is created BEFORE any inventory exists
    notebook = PhysicalProduct("P002", "Notebook", 4.50, 50, supplier, 0.3)

    inventory_a = Inventory()
    inventory_b = Inventory()

    inventory_a.add_product(notebook)
    print("In A after adding?", inventory_a.find_product("P002") is not None)

    # Predict first: does the product still work after removal?
    inventory_a.remove_product("P002")
    print("In A after removing?", inventory_a.find_product("P002") is not None)
    print("Product still usable after removal:")
    notebook.display_information()

    inventory_b.add_product(notebook)
    print("\nIn B now?", inventory_b.find_product("P002") is not None)
    print("Same object in B?", inventory_b.find_product("P002") is notebook)


def test_composition() -> None:
    print("\n===== 4. COMPOSITION: Order - OrderLine =====")
    supplier = Supplier("S001", "TechWorld Pte Ltd", "sales@techworld.sg")
    laptop = PhysicalProduct("P001", "Laptop", 1299.90, 10, supplier, 1.8)
    ebook = DigitalProduct("D001", "Python eBook", 19.90, 100, supplier, 25.5)

    order1 = Order("O001")
    order1.add_order_line(laptop, 1)   # Order creates the OrderLine itself
    order1.add_order_line(ebook, 3)
    order1.display_order()

    # Predict first: same product in two orders -> how many lines / products?
    order2 = Order("O002")
    order2.add_order_line(laptop, 2)
    print()
    order2.display_order()
    print("\n2 orders each made their own OrderLine, but both point to ONE laptop object")
    print("laptop id:", id(laptop))

    print("\nRemoving the ebook line from O001:")
    order1.remove_order_line("D001")
    order1.display_order()


def test_lsp_and_polymorphism() -> None:
    print("\n===== 6 & 7. LSP + POLYMORPHISM =====")
    supplier = Supplier("S001", "TechWorld Pte Ltd", "sales@techworld.sg")
    laptop = PhysicalProduct("P001", "Laptop", 1299.90, 10, supplier, 1.8)
    ebook = DigitalProduct("D001", "Python eBook", 19.90, 100, supplier, 25.5)

    print("show_product_details() with a PhysicalProduct:")
    show_product_details(laptop)
    print("\nshow_product_details() with a DigitalProduct:")
    show_product_details(ebook)

    # Both types in ONE inventory, ONE loop, no isinstance()
    inventory = Inventory()
    inventory.add_product(laptop)
    inventory.add_product(ebook)

    # Predict first: what will each get_fulfilment_info() print?
    print("\nLooping over the Product collection:")
    for product in inventory.get_products():
        product.display_information()
        print(product.get_fulfilment_info())
        print("-" * 20)

    # Both subclasses keep update_stock()'s meaning (LSP)
    laptop.update_stock(5)
    ebook.update_stock(5)
    print("Both accepted update_stock(5) with the same behaviour as Product.")


if __name__ == "__main__":
    test_association()
    test_aggregation()
    test_composition()
    test_lsp_and_polymorphism()
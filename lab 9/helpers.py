import csv
from inventory import Inventory
from productfactory import ProductFactory
from supplier import Supplier

def get_positive_float(prompt: str) -> float:
    """Keeps asking until the user enters a number greater than zero."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)  # skip header row
            for row_number, row in enumerate(reader, start=2):
                try:
                    product_type, product_id, name, price, stock = row
                    product = ProductFactory.create(
                        product_type.strip(), product_id.strip(), name.strip(),
                        float(price), int(stock), supplier
                    )
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as error:
                    print(f"Row {row_number} skipped: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
import json
import os
from product import Product
from productfactory import ProductFactory
from helpers import get_positive_float
from inventory import Inventory
from supplier import Supplier

FILENAME = "inventory.json"

# One Supplier object per supplier ID, shared by all its products (association)
suppliers: dict[str, Supplier] = {}

def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Remove Product")
    print("6. Save Inventory")
    print("7. Exit")
    print("----------------------------")

def get_or_create_supplier(supplier_id: str, name: str, contact_email: str) -> Supplier:
    """Reuse the existing Supplier object if we've seen this ID before."""
    if supplier_id not in suppliers:
        suppliers[supplier_id] = Supplier(supplier_id, name, contact_email)
    return suppliers[supplier_id]

def save_inventory(inventory: Inventory) -> None:
    with open(FILENAME, "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

def load_inventory() -> Inventory:
    inventory = Inventory()

    if os.path.exists(FILENAME):
        print(f"{FILENAME} found.")

        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)

            for item in data:
                s = item.get("supplier", {"id": "S000", "name": "Unknown Supplier", "contact_email": "-"})
                supplier = get_or_create_supplier(s["id"], s["name"], s["contact_email"])

                try:
                    product = ProductFactory.create(
                        item["type"],
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        supplier,
                        item.get("weight", item.get("download_size", 0.0))
                    )
                except ValueError as error:
                    print(f"Skipping product: {error}")
                    continue

                inventory.add_product(product)

            print("Inventory loaded successfully.")

        except json.JSONDecodeError:
            print(f"{FILENAME} is corrupted. Starting with an empty inventory.")

    else:
        print(f"{FILENAME} not found. Starting with an empty inventory.")

    return inventory

def ask_existing_product(inventory: Inventory) -> Product | None:
    """Keep asking until a valid Product ID is entered. Blank = cancel."""
    while True:
        product_id = input("Enter Product ID (or press Enter to cancel): ").strip().upper()
        if product_id == "":
            return None
        product = inventory.find_product(product_id)
        if product is not None:
            return product
        print("Product not found. Please try again.")

def ask_supplier() -> Supplier:
    while True:
        supplier_id = input("Supplier ID: ").strip().upper()
        if supplier_id != "":
            break
        print("Please enter a Supplier ID")
 
    if supplier_id in suppliers:
        print(f"Using existing supplier: {suppliers[supplier_id].get_name()}")
        return suppliers[supplier_id]
 
    name = input("Supplier Name: ").strip()
    contact_email = input("Supplier Email: ").strip()
    return get_or_create_supplier(supplier_id, name, contact_email)

def add_product(inventory: Inventory) -> None:
    print("\nAdd New Product")

    while True:
        product_id = input("Product ID: ").strip().upper()
        if product_id == "":
            print("Please enter a Product ID")
        elif inventory.find_product(product_id):
            print("Product ID already exists. Enter a different ID.")
        else:
            break

    while True:
        product_name = input("Product Name: ").strip()
        if product_name != "":
            break
        print("Enter a Product Name")

    price = get_positive_float("Price: ")

    while True:
        try:
            stock = int(input("Stock Quantity: "))
            if stock >= 0:
                break
            print("Stock cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")
    
    supplier = ask_supplier()

    print("\nSelect Product Type")
    print("1. Physical Product")
    print("2. Digital Product")

    while True:
        choice = input("Enter option: ").strip()
        if choice == "1":
            product_type, label = "physical", "Enter weight (kg): "
            break
        elif choice == "2":
            product_type, label = "digital", "Enter download size (MB): "
            break
        print("Invalid option. Please select 1 or 2.")

    extra = get_positive_float(label)
    product = ProductFactory.create(
        product_type, product_id, product_name, price, stock, supplier, extra
    )

    inventory.add_product(product)
    print("\nProduct added successfully!")

def update_stock(inventory: Inventory) -> None:
    print("\nUpdate Stock")
    product = ask_existing_product(inventory)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    product.display_information()

    while True:
        try:
            quantity = int(input("\nEnter quantity to change (e.g. 5 or -2): "))
            break
        except ValueError:
            print("Please enter a whole number.")

        try:
            product.update_stock(quantity)
            print("\nStock updated successfully!")
        except ValueError as error:
            print(f"\n{error}")

def search_product(inventory: Inventory) -> None:
    print("\nSearch Product")

    product = ask_existing_product(inventory)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    product.display_information()

def remove_product(inventory: Inventory) -> None:
    print("\nRemove Product")
    product = ask_existing_product(inventory)
    if product is None:
        print("\nProduct not found.")
        return
    inventory.remove_product(product.get_product_id())
    print("\nProduct removed from inventory.")

def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================\n")

    inventory = load_inventory()

    while True:
        show_menu()
        choice = input("\nEnter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            remove_product(inventory)

        elif choice == "6":
            print("\nSaving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {FILENAME}.")

        elif choice == "7":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option, try again.")
            show_menu()


if __name__ == "__main__":
    main()
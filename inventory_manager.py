import json
import os

FILENAME = "inventory.json"

def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def save_inventory(inventory):
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)


def load_inventory():
    if os.path.exists(FILENAME):
        print(f"{FILENAME} found.")
        try:
            with open(FILENAME, "r") as file:
                inventory = json.load(file)
            print("Inventory loaded successfully.")
            return inventory
        except json.JSONDecodeError:
            print(f"{FILENAME} is corrupted. Starting with an empty inventory.")
            return []
    else:
        print(f"{FILENAME} not found. Starting with an empty inventory.")
        return []


def find_product(inventory, product_id):
    for product in inventory:
        if product["id"].upper() == product_id.upper():
            return product
    return None


def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")
    if not inventory:
        print("No products in inventory.")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | "
              f"Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("------------------------------------------------")


def add_product(inventory):
    print("\nAdd New Product")

    while True:
        product_id = input("Product ID: ").strip().upper()
        if product_id == "":
            print("Please enter a Product ID")
        elif find_product(inventory, product_id):
            print("Product ID already exists. Enter a different ID.")
        else:
            break

    while True:
        product_name = input("Product Name: ").strip()
        if product_name != "":
            break
        print("Enter a Product Name")

    while True:
        try:
            price = float(input("Price: "))
            if price >= 0:
                break
            print("Price cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            stock = int(input("Stock Quantity: "))
            if stock >= 0:
                break
            print("Stock cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")

    inventory.append({"id": product_id, "name": product_name, "price": price, "stock": stock})
    print("\nProduct added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()
    product = find_product(inventory, product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    while True:
        try:
            new_stock = int(input("\nNew Stock Quantity: "))
            if new_stock >= 0:
                break
            print("Stock cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")

    product["stock"] = new_stock
    print("\nStock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = find_product(inventory, product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("------------------------------------------------")
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("------------------------------------------------")


def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================\n")

    inventory = load_inventory()

    show_menu()
    while True:
        choice = input("\nEnter option: ").strip()

        if choice == "1":
            display_all(inventory)

        elif choice == "2":
            add_product(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {FILENAME}.")

        elif choice == "6":
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

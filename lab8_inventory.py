import json
import os

FILENAME = "inventory.json"

"""
Identify Objects
_____________________________________
Product                              |   <-- Class Name
_____________________________________|
- __product_id: String               |    
- __name: String                     |   <-- Attributes
- __price: float                     |
- __stock: int                       |
_____________________________________|
+ get_product_id(): void             |
+ update_stock(quantity : int): void |   <-- Methods
+ display_information(): void        |
+ to_dict(): dict                    |
_____________________________________|

Access modifiers (who can see / use it)
______________________
+: public --> accessible from anywhere (inside and outside the class)
e.g self.myvar 

-: private --> only inside the same class
e.g self.__myvar

#: protected --> the class itself and its child classes
e.g self._myvar
"""

class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity: int):
        if self.__stock + quantity < 0:
            print("Not enough stock!")
            return
        self.__stock += quantity

    def display_information(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

    def to_dict(self):
        """Converts this product into a dictionary so it can be saved as JSON.
        Keys match the old file format, so an existing inventory.json still loads. """ 
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}

"""
inventory.add_product(product1) # pass the product to inventory class to store in a list
^ Hints to use list
_____________________________________
Inventory                            |   <-- Class Name
_____________________________________|   
- __products: list[Products]         |   <-- Attributes
_____________________________________|
+ add_product(product: Product)      |   <-- Methods
+ search_product(product_id: str)    |
+ display_all()                      |
+ to_list(): list[dict]              |
_____________________________________|
"""
class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product):
        self.__products.append(product)

    def search_product(self, product_id: str):
        for product in self.__products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return
        
        for product in self.__products:
            product.display_information()
            print("-" * 20)

    def to_list(self):
        # Converts every Product into a dictionary for saving.
        return [product.to_dict() for product in self.__products]

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
        json.dump(inventory.to_list(), file, indent=4)

def load_inventory():
    inventory = Inventory()
    if os.path.exists(FILENAME):
        print(f"{FILENAME} found.")
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
            # JSON gives back dictionaries, so turn each one into a Product object
            for item in data:
                inventory.add_product(Product(item["id"], item["name"], item["price"], item["stock"]))
            print("Inventory loaded successfully.")
        except json.JSONDecodeError:
            print(f"{FILENAME} is corrupted. Starting with an empty inventory.")
    else:
        print(f"{FILENAME} not found. Starting with an empty inventory.")
    return inventory

def add_product(inventory):
    print("\nAdd New Product")

    while True:
        product_id = input("Product ID: ").strip().upper()
        if product_id == "":
            print("Please enter a Product ID")
        elif inventory.search_product(product_id):
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

    product = Product(product_id, product_name, price, stock)
    inventory.add_product(product)
    print("\nProduct added successfully!")

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    product.display_all()

    while True:
        try:
            quantity = int(input("\nNew Stock Quantity: "))
            if quantity >= 0:
                break
            print("Stock cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")

    product.update_stock(quantity)
    print("\nStock updated successfully!")

def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    product.display_information()

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

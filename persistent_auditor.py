import random
import ast

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            print("Inventory loaded.")
            for line in file:
                data = ast.literal_eval(line.strip())
                for order in data:
                    print(*order, sep=", ")
            return data
    except FileNotFoundError:
        print("inventory.txt file does not exist.")
        return ""

def save_inventory(tracker):
    if tracker == []:
       print("No new product added.")
    else:
        with open("inventory.txt", "a") as file:
            file.write(f"{tracker}\n")
            print("Order successfully saved to inventory.txt")

def get_valid_input():
    tracker = []
    inventory = load_inventory()

    while True:
        product_name = input("\nEnter Product Name (or quit): ")

        if product_name.lower() == "quit":
            save_inventory(tracker)
            break
        elif product_name.strip == "":
            print("Please enter a product name")
        else:
            quantity = input("Enter Quantity: ")
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                orderID = random.randint(1001, 9999)
                tracker.append([orderID,product_name,quantity])
                print("\nNew Order Added:")
                print(f"{orderID}, {product_name}, {quantity}")
            else:
                print("Please enter a positive quantity.")

get_valid_input()
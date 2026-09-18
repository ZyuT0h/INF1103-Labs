def get_valid_input():
    inventory = 0
    fail_counter = 0
    delivery_counter = 0

    while True:
        user_input = input("Enter a stock quantity (or quit to exit): ")

        if user_input.lower() == "quit":
            generate_report(inventory,fail_counter)
            print(f"Total Deliveries Processed: {delivery_counter}")
            break
        elif not user_input.isdigit():
            print("Please input integers only.")
            fail_counter += 1
        else:
            stock = int(user_input)
            if stock < 0:
                print("Negative numbers are not allowed")
                fail_counter += 1
            else:
                inventory += stock
                calculate_tax(process_delivery(inventory,stock))
                delivery_counter += 1
            if inventory > 500:
                print("ALERT! Overstocked!")
                fail_counter += 1
                break

    return user_input

def process_delivery(current_total, new_value):
    print(f"Old Total: {current_total} ")
    new_value =+ current_total
    print(f"New Total: {new_value}")
    return new_value

def calculate_tax(amount):
    tax = 0.1
    tax = amount * tax
    return tax

def generate_report(total_units, failed_attempts):
    print (f"Total United Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

get_valid_input()
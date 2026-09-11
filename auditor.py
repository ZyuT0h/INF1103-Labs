inventory = 0
fail_counter = 0

while True:
    user_input = input("Enter a stock quantity (or quit to exit): ")

    if user_input.lower() == "quit":
        print(f"Total Units Processed: {inventory}")
        print(f"Number of Failed/Rejected Entries: {fail_counter}")
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
            print(f"Total Units Processed: {inventory}")
        if inventory > 500:
            print("ALERT! Overstocked!")
            fail_counter += 1
            break
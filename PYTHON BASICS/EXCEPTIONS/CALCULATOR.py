def show_menu(current_number):
    print("\n--- Calculator ---")
    print("Current number:", current_number)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")


def get_number():
    value = input("Enter a number: ")
    try:
        return float(value)
    except:
        print("Error: Invalid number.")
        return None


def add(current, value):
    return current + value


def subtract(current, value):
    return current - value


def multiply(current, value):
    return current * value


def divide(current, value):
    if value == 0:
        print("Error: Cannot divide by zero.")
        return None
    return current / value


def calculator():
    current_number = 0

    while True:
        show_menu(current_number)
        option = input("Choose an option: ")

        # Validate menu option
        try:
            option = int(option)
        except:
            print("Error: Invalid option.")
            continue

        if option == 6:
            print("Exiting calculator...")
            break

        if option < 1 or option > 6:
            print("Error: Option not in menu.")
            continue

        if option == 5:
            current_number = 0
            print("Result cleared.")
            continue

        # Get number for operation
        new_value = get_number()
        if new_value is None:
            continue

        # Perform operation
        if option == 1:
            current_number = add(current_number, new_value)
        elif option == 2:
            current_number = subtract(current_number, new_value)
        elif option == 3:
            current_number = multiply(current_number, new_value)
        elif option == 4:
            result = divide(current_number, new_value)
            if result is None:
                continue
            current_number = result

        print("New current number:", current_number)


# Start the calculator
calculator()

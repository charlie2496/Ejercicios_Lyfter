current_number = 0

while True:
    print("\n--- Calculator ---")
    print("Current number:", current_number)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")
    option = input("Choose an option: ")
    try:
        option = int(option)
    except:
        print("Error: Invalid option. Please enter a number from the menu.")
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

    new_value = input("Enter a number: ")

    try:
        new_value = float(new_value)
    except:
        print("Error: Invalid number. Operation cancelled.")
        continue

    if option == 1:
        current_number += new_value
    elif option == 2:
        current_number -= new_value
    elif option == 3:
        current_number *= new_value
    elif option == 4:
        if new_value == 0:
            print("Error: Cannot divide by zero.")
            continue
        current_number /= new_value

    print("New current number:", current_number)

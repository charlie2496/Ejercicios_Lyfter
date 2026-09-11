number_1=float(input("Enter a number: "))
number_2=float(input("Enter another number: "))
print(f"\nOriginal numbers: {number_1} and {number_2}")
if number_1==number_2:
    print("The numbers are equal.")
else:
    if number_1>number_2:
        number_1, number_2 = number_2, number_1
    print(f"ordered values → A:{number_1}, B:{number_2}.")
    
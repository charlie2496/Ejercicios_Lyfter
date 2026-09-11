number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

if number_1 > number_2 and number_1 > number_3:
    print("The largest number is:", number_1)
elif number_2 > number_1 and number_2 > number_3:
    print("The largest number is:", number_2)
elif number_3 > number_1 and number_3 > number_2:
    print("The largest number is:", number_3)
else:
    print("You cannot enter equal numbers.")
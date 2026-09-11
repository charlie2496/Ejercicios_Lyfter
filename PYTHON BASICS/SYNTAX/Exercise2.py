first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello {first_name} {last_name}")
age = int(input("Enter your age: "))

if age <= 3:
    print(f"Welcome {first_name} {last_name}, you are a baby.")
elif age <= 10:
    print(f"Welcome {first_name} {last_name}, you are a child.")
elif age <= 13:
    print(f"Welcome {first_name} {last_name}, you are a pre-teen.")
elif age <= 18:
    print(f"Welcome {first_name} {last_name}, you are a teenager.")
elif age <= 40:
    print(f"Welcome {first_name} {last_name}, you are a young adult.")
elif age <= 60:
    print(f"Welcome {first_name} {last_name}, you are an adult.")
else:
    print(f"Welcome {first_name} {last_name}, you are a senior adult.")
print("Thank you for using our program!")
print("Goodbye!")
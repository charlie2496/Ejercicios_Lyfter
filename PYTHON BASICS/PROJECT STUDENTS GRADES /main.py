def display_menu():
    print("Welcome to the Student Grades Management System")
    print("Please select an option:")
    print("1. Add a new student")
    print("2. View all students")
    print("3. View failed students")
    print("4. View top 3 students")
    print("5. Delete a student")
    print("6. Exit")
    return input("Enter your choice (1-5): ")
if input("Enter your choice (1-5): ") == "1":
    open("menu.py", "r", encoding="utf-8").read(add_student())
elif input("Enter your choice (1-5): ") == "2":
    open("menu.py", "r", encoding="utf-8").read(view_students())
elif input("Enter your choice (1-5): ") == "3":
    open("menu.py", "r", encoding="utf-8").read(view_failed_students())
elif input("Enter your choice (1-5): ") == "4":
    open("menu.py", "r", encoding="utf-8").read(view_top_students())
elif input("Enter your choice (1-5): ") == "5":
    open("menu.py", "r", encoding="utf-8").read(delete_student())
elif input("Enter your choice (1-5): ") == "6":
    print("Exiting the program. Goodbye!")
else:
    print("Invalid choice. Please try again.")

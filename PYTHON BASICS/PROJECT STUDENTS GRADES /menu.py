import actions
import data
def show_menu():

    while True:
        print("Welcome to the Student Grades Management System")
        print("Please select an option:")
        print("1. Add a new student")
        print("2. View all students")
        print("3. View failed students")
        print("4. View top 3 students")
        print("5. Delete a student")
        print("6. Exit")
        print("7. Export students to CSV")
        print("8. View general average")
        print("9. Import students from CSV")
        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            student = actions.add_student()
            data.students.append(student)
            print("Student added successfully")
            print(data.students)

        elif choice == "2":
            actions.view_students(data.students)
        elif choice == "3":
            actions.view_failed_students(data.students)
        elif choice == "4":
            actions.view_top_3_students(data.students)
        elif choice == "5":
            actions.delete_student(data.students)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        elif choice == "7":
            data.export_students(data.students)
        elif choice == "8":
                actions.view_general_average(data.students)
        elif choice == "9":
                data.import_students()
        else:
            print("Invalid choice. Please try again.")


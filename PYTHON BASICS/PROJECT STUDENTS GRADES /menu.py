
def add_student():
    name = input("Enter the student's name: ")
    section = input("Enter the student's section: ")
    spanish_grade = input("Enter the student's Spanish grade: ")
    english_grade = input("Enter the student's English grade: ")
    social_studies_grade = input("Enter the student's Social Studies grade: ")
    science_grade = input("Enter the student's Science grade: ")


def view_students():
        with open("data.txt", "r", encoding="utf-8") as file:
            students_grades= file.readlines()
        print("Student Grades:")


def view_failed_students():
        with open("data.txt", "r", encoding="utf-8") as file:
            students = file.readlines()
print("Failed Students:")


def view_top_students():
        with open("data.txt", "r", encoding="utf-8") as file:
            students = file.readlines()
        print("Top 3 Students:")

def delete_student():
    delete_student = input("Enter the name of the student to delete: ")
    confirmation = input(f"Are you sure you want to delete '{delete_student}'? (y/n): ")
        if confirmation.lower() == "y":  
        else:
            print("Deletion canceled.")
        with open("actions.py ", "r", encoding="utf-8") as file:
            students = file.readlines()
        delete_student()
    print(f"Student '{delete_student}' has been deleted.")

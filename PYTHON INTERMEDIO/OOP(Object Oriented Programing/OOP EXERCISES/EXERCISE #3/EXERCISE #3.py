import csv

def show_menu(students):

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
            student = add_student()
            students.append(student)
            print("Student added successfully")

        elif choice == "2":
            view_students(students)
        elif choice == "3":
            view_failed_students(students)
        elif choice == "4":
            view_top_3_students(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        elif choice == "7":
            export_students(students)
        elif choice == "8":
                view_general_average(students)
        elif choice == "9":
                import_students(students)
        else:
            print("Invalid choice. Please try again.")



class Student:
    def __init__(self, name, section, spanish_grade, english_grade, social_studies_grade, science_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade

def add_student():
    while True:
        name = input("enter the student's name:").strip()
        if name:
            break
        print("please enter a valid name")
    while True:
        section = input("Enter the student's section: ").strip().upper()

        if (
        len(section) >= 2
        and section[:-1].isdigit()
        and section[-1].isalpha()
    ):
            break

        print("Please enter a valid section (ex: 10B, 11A).")
    
    while True:
            try:
                spanish_grade = float(input("Enter the student's Spanish grade: "))
                if spanish_grade >= 0 and spanish_grade <= 100:
                    break
                else:
                    print("Please enter a valid number between 0 and 100 for Spanish grade.")
            except ValueError:
                print("Please enter a valid number for Spanish grade.")
    while True:       
            try:
                english_grade = float(input("Enter the student's English grade: "))
                if english_grade >= 0 and english_grade <= 100:
                    break
                else:
                    print("Please enter a valid number between 0 and 100 for English grade.")
            except ValueError:
                print("Please enter a valid number for English grade.")
    while True:
            try:
                social_studies_grade = float(input("Enter the student's Social Studies grade: "))
                if social_studies_grade >= 0 and social_studies_grade <= 100:
                    break
                else:
                    print("Please enter a valid number between 0 and 100 for Social Studies grade.")
            except ValueError:
                print("Please enter a valid number for Social Studies grade.")
    while True:
            try:
                science_grade = float(input("Enter the student's Science grade: "))

                if 0 <= science_grade <= 100:
                    break
                else:
                    print("Please enter a valid number between 0 and 100 for Science grade.")

            except ValueError:
                print("Please enter a valid number for Science grade.")

    student_data = Student(
        name,
        section,
        spanish_grade,
        english_grade,
        social_studies_grade,
        science_grade
    )
    return student_data   


def view_students(students):
    if not students:
        print("No students registered.")
        return

    for student in students:
        print(f"Name: {student.name}")
        print(f"Section: {student.section}")
        print(f"Spanish: {student.spanish_grade}")
        print(f"English: {student.english_grade}")
        print(f"Social Studies: {student.social_studies_grade}")
        print(f"Science: {student.science_grade}")
        print("------------------------")

def view_failed_students(students):
        
        failed_students = []
        for student in students:
            if (
                student.spanish_grade < 60
                or student.english_grade < 60
                or student.social_studies_grade < 60
                or student.science_grade < 60
            ):
                failed_students.append(student)

        if failed_students:
            for student in failed_students:
                print(f'Name: {student.name}')
                print(f'Section: {student.section}')
                print("Failed Subjects:")
                if student.spanish_grade < 60:
                    print(f' - Spanish: {student.spanish_grade}')
                if student.english_grade < 60:
                    print(f' - English: {student.english_grade}')
                if student.social_studies_grade < 60:
                    print(f' - Social Studies: {student.social_studies_grade}')
                if student.science_grade < 60:
                    print(f' - Science: {student.science_grade}')
        else:
            print("No failed students found.")

def view_top_3_students(students):
        student_averages = []
        for student in students:
            name = student.name
            section = student.section
            spanish_grade = student.spanish_grade
            english_grade = student.english_grade
            social_studies_grade = student.social_studies_grade
            science_grade = student.science_grade

            average = (
                spanish_grade + english_grade + social_studies_grade + science_grade
            ) / 4
            student_averages.append(
                {
                    "name": name,
                    "section": section,
                    "average": average,
                }
            )

        top_students = sorted(
            student_averages, key=lambda x: x["average"], reverse=True
        )[:3]

        if not top_students:
            print("No students registered.")
        else:
            print("top 3 students:")

            for student in top_students:
                print(f"Name:{student['name']}")
                print(f"section:{student['section']}")
                print(f"Average:{student['average']:.2f}")
                print("---------------------------------")

        return top_students

def delete_student(students):

    name = input("Enter the name of the student to delete: ").strip().lower()
    Section = input("Enter the student section:").strip().upper()

    for student in students:
        if (
            student.name.lower() == name
            and student.section == Section
        ):
            print("student found!")
            
            confirmation = input("Are you sure you want to delete? Enter Y for yes or N to cancel: ").strip().upper()

            if confirmation == "Y":
                students.remove(student)
                print("Student deleted successfully!!")
            else:
                print("Deletion cancelled")

            break
    else:
        print("student not found")

def view_general_average(students):
    if not students:
        print("No students registered")
        return

    total_average = 0
    for student in students:
        spanish_grade = student.spanish_grade
        english_grade = student.english_grade
        social_studies_grade = student.social_studies_grade
        science_grade = student.science_grade
        student_average = (spanish_grade + english_grade + social_studies_grade + science_grade)/4
        total_average = total_average + student_average
    general_average = total_average / len(students)
    print(" The average score of the class is:", general_average)

def export_students(students):
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "name",
            "section",
            "spanish_grade",
            "english_grade",
            "social_studies_grade",
            "science_grade"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            student_data = {
                "name": student.name,
                "section": student.section,
                "spanish_grade": student.spanish_grade,
                "english_grade": student.english_grade,
                "social_studies_grade": student.social_studies_grade,
                "science_grade": student.science_grade
            }

            writer.writerow(student_data)

    print("Students exported successfully")




def import_students(students):
    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    row["name"],
                    row["section"],
                    float(row["spanish_grade"]),
                    float(row["english_grade"]),
                    float(row["social_studies_grade"]),
                    float(row["science_grade"])
                )

                students.append(student)

        print("Students imported successfully!")

    except FileNotFoundError:
        print("The CSV file was not found.")

    except (ValueError, KeyError) as error:
        print(f"Error importing students: {error}")

if __name__ == "__main__":
    students = []
    show_menu(students)
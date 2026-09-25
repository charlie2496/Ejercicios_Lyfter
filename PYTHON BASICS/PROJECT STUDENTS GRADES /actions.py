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

    student_data = {
        "name": name,
        "section": section,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "social_studies_grade": social_studies_grade,
        "science_grade": science_grade
    }

    return student_data

        
def view_students(students):
    if not students:
        print("No students registered.")
        return

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish: {student['spanish_grade']}")
        print(f"English: {student['english_grade']}")
        print(f"Social Studies: {student['social_studies_grade']}")
        print(f"Science: {student['science_grade']}")
        print("------------------------")



def view_failed_students(students):
        
        failed_students = []
        for student in students:
            if (
                student["spanish_grade"] < 60
                or student["english_grade"] < 60
                or student["social_studies_grade"] < 60
                or student["science_grade"] < 60
                ):
                failed_students.append(student)
                if failed_students:
                    for student in failed_students:
                        print(student)
                else:
                    print("No failed students found.")

def view_top_3_students(students):
        student_averages = []
        for student in students:
            name = student["name"]
            section = student["section"]
            spanish_grade = student["spanish_grade"]
            english_grade = student["english_grade"]
            social_studies_grade = student["social_studies_grade"]
            science_grade = student["science_grade"]

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
            student["name"].lower() == name
            and student["section"] == Section
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
        spanish_grade = student["spanish_grade"]
        english_grade = student["english_grade"]
        social_studies_grade = student["social_studies_grade"]
        science_grade = student["science_grade"]
        student_average = (spanish_grade + english_grade + social_studies_grade + science_grade)/4
        total_average = total_average + student_average
    general_average = total_average / len(students)
    print(" The average score of the class is:", general_average)
    


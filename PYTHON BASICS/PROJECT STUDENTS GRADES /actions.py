def open_file():
    try:
        with open("menu.py", "r", encoding="utf-8") as add_student:
            menu_content = add_student.read()

        if (
            name is None
            or section is None
            or spanish_grade is None
            or english_grade is None
            or social_studies_grade is None
            or science_grade is None
        ):
            print(
                f"Student {name} is missing information to enter therefore it will not be added to the list of students."
            )
        elif (
            spanish_grade < 0
            or english_grade < 0
            or social_studies_grade < 0
            or science_grade < 0
            or spanish_grade > 100
            or english_grade > 100
            or social_studies_grade > 100
            or science_grade > 100
        ):
            print(
                f"Student {name} has grades that are not within the valid range (0-100)."
            )
        elif section not in ["number", "letter"]:
            print(
                f"Student {name} has an invalid section. Please enter a number and then a letter (ex: 10B, 11A)."
            )
        else:
            student = {
                "name": name,
                "section": section,
                "spanish_grade": spanish_grade,
                "english_grade": english_grade,
                "social_studies_grade": social_studies_grade,
                "science_grade": science_grade,
            }

            with open("data.txt", "w", encoding="utf-8") as file:
                for student in student_grades:
                    file.write(
                        f"{student['name']},{student['section']},{student['spanish_grade']},{student['english_grade']},{student['social_studies_grade']},{student['science_grade']}\n"
                    )

        return menu_content

    except FileNotFoundError:
        print("The file 'menu.py' was not found.")




def view_failed_students():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            students = file.readlines()

        failed_students = []
        for student in students:
            name, section, spanish_grade, english_grade, social_studies_grade, science_grade = student.strip().split(
                ","
            )
            spanish_grade = float(spanish_grade)
            english_grade = float(english_grade)
            social_studies_grade = float(social_studies_grade)
            science_grade = float(science_grade)

            if (
                spanish_grade < 60
                or english_grade < 60
                or social_studies_grade < 60
                or science_grade < 60
            ):
                failed_students.append(
                    {
                        "name": name,
                        "section": section,
                        "spanish_grade": spanish_grade,
                        "english_grade": english_grade,
                        "social_studies_grade": social_studies_grade,
                        "science_grade": science_grade,
                    }
                )

        return failed_students
    with open("data.txt", "w", encoding="utf-8") as file:
        for student in failed_students:
            file.write(
                f"{student['name']},{student['section']},{student['spanish_grade']},{student['english_grade']},{student['social_studies_grade']},{student['science_grade']}\n"
            )
    except FileNotFoundError:
        print("The file 'data.txt' was not found.")


def view_top_3_students():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            students = file.readlines()

        student_averages = []
        for student in students:
            name, section, spanish_grade, english_grade, social_studies_grade, science_grade = student.strip().split(
                ","
            )
            spanish_grade = float(spanish_grade)
            english_grade = float(english_grade)
            social_studies_grade = float(social_studies_grade)
            science_grade = float(science_grade)

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

        return top_students
    except FileNotFoundError:
        print("The file 'data.txt' was not found.")


def delete_student():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            students = file.readlines()

        student_name = input("Enter the name of the student to delete: ")
        student_name = student_name.strip() 
        updated_students = [
            student for student in students if not student.startswith(student_name)
        ]

        with open("data.txt", "w", encoding="utf-8") as file:
            file.writelines(updated_students)

        print(f"Student {student_name} has been deleted.")
    except FileNotFoundError:
        print("The file 'data.txt' was not found.")
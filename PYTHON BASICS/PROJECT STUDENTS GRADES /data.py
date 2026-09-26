import csv

students = []


def export_students(students):
    with open("students.csv","w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "name",
            "section",
            "spanish_grade",
            "english_grade",
            "social_studies_grade",
            "science_grade"
        ]
        writer=csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    print("students exported successfully")

def import_students():
    try:
        with open("students.csv", "r", encoding="utf-8") as file:
            reader =csv.DictReader(file)
            for student in reader:
                student["spanish_grade"] = float(student["spanish_grade"])
                student["english_grade"] = float(student["english_grade"])
                student["social_studies_grade"] = float(student["social_studies_grade"])
                student["science_grade"] = float(student["science_grade"])
                for existing_student in students:
                    if student["name"] == existing_student["name"] and student["section"] == existing_student["section"]:
                        
                        break
                else:
                    students.append(student)
        print("Students imported successfully")            
    except FileNotFoundError:
        print("No exported CSV file was found")


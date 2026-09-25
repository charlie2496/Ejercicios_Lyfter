import csv

students = [
    {
        "name": "Carlos",
        "section": "10A",
        "spanish_grade": 90.0,
        "english_grade": 85.0,
        "social_studies_grade": 95.0,
        "science_grade": 90.0
    },
    {
        "name": "Maria",
        "section": "11B",
        "spanish_grade": 70.0,
        "english_grade": 80.0,
        "social_studies_grade": 75.0,
        "science_grade": 75.0
    },
    {
        "name": "Pedro",
        "section": "10B",
        "spanish_grade": 95.0,
        "english_grade": 95.0,
        "social_studies_grade": 100.0,
        "science_grade": 90.0
    },
    {
        "name": "Ana",
        "section": "11A",
        "spanish_grade": 80.0,
        "english_grade": 85.0,
        "social_studies_grade": 80.0,
        "science_grade": 95.0
    }
]


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


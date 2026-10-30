def decorator_name(func):
    def average_score(parameters):
        spanish_score = int(input("enter Spanish score: "))
        english_score = int(input("enter English score: "))

        func(parameters) 
        average_score = (spanish_score + english_score) / 2
        print("The average score is:", average_score)
        return average_score

    return average_score


@decorator_name
def show_student_info(student):
    print(f"Student: {student}")


show_student_info("Carlos Andres")

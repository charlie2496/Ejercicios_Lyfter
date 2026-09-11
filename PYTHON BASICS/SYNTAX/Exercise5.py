total_grades= int(input("Enter the total number of grades: "))
grades_counter=1
passed_grades=0
failed_grades=0
sum_passed_grades=0
sum_failed_grades=0
sum_total_grades=0
while grades_counter <= total_grades:
    grade = float(input(f"Enter grade {grades_counter}: "))
    if grade >= 70:
        passed_grades += 1
        sum_passed_grades += grade
    else:
        failed_grades += 1
        sum_failed_grades += grade
    sum_total_grades += grade
    grades_counter += 1 
if passed_grades > 0:
    average_passed= sum_passed_grades/ passed_grades
else:
    average_passed = 0
if failed_grades > 0:
    average_failed = sum_failed_grades / failed_grades
else:
    average_failed = 0  
average_total= sum_total_grades / total_grades if total_grades > 0 else 0
print(f"Total number of grades: {total_grades}")
print(f"Number of passed grades: {passed_grades}") 
print(f"Average of passed grades: {average_passed:.2f}")
print(f"Number of failed grades: {failed_grades}")
print(f"Average of failed grades: {average_failed:.2f}")
print(f"total average of all grades: {sum_total_grades / total_grades:.2f}")
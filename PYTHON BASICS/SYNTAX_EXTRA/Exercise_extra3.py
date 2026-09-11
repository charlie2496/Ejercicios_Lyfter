Enter_a_number=float(input("Enter a number: "))
counter=1
Add=0
sum_text=""
while Enter_a_number >= counter:
    Add+= counter
    if counter == Enter_a_number:
        sum_text += f" {counter}"
    else:
        sum_text += f" {counter} + "
    counter += 1
print(f"{Enter_a_number}→ {Add} = {sum_text}")

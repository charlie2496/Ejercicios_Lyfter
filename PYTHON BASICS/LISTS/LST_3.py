counter=0
largest_number=0
my_list = []
while counter < 10:
    item = int(input("Ingrese un número: "))
    my_list.append(item)
    counter += 1
    if item > largest_number:
        largest_number = item
    else:
        largest_number = largest_number
print(my_list, "→ El número mayor es:", largest_number)
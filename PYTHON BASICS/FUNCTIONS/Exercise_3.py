list_of_numbers = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
def sum_numbers_list(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number
    return total

print(sum_numbers_list(list_of_numbers))
numbers_list = [1, 4, 6, 7, 13, 9, 67]

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
print(list(filter(is_prime, numbers_list)))
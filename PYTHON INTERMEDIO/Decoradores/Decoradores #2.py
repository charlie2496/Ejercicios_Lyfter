def numbers_only(func):
        def wrapper(*args):
                if len(args) != 5:
                        raise ValueError("Enter exactly 5 numbers")
                for number in args:
                        int(number)
                return func(*args)
        return wrapper

@numbers_only
def lottery(a, b, c, d, e):
        return [a, b, c, d, e]

try:
        numbers = input("Enter 5 numbers separated by commas: ")
        numbers = numbers.split(",")
        print(lottery(*numbers))
except ValueError:
        print("Error: Enter exactly 5 valid numbers")



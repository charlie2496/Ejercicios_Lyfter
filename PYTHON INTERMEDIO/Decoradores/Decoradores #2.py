
def numbers_only(func):
        def wrapper(*args):
                for number in args:
                        if type(number) not in (int, float):
                                raise TypeError("Only numbers allowed")
                return func(*args)
        return wrapper

@numbers_only
def lottery(a, b, c, d, e):
        return [a, b, c, d, e]

try:
        numbers = input("Enter 5 numbers separated by commas: ")
        numbers = [int(x) for x in numbers.split(",")]

        if len(numbers) != 5:
                raise ValueError("Enter exactly 5 numbers")

        print(lottery(*numbers))
except (ValueError, TypeError) as error:
        print("Error:", error)

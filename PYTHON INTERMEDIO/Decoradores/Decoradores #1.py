
def decorator_name(func):
    def wrapper(*args):
        print("Parameters:", args)
        result = func(*args)
        print("Return:", result)
        return result
    return wrapper

@decorator_name
def average_score(spanish, english):
    return (spanish + english) / 2

average_score(90, 80)

from datetime import datetime, date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        birth = datetime.strptime(self.date_of_birth, "%d/%m/%Y").date()
        today = date.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))


def adult_only(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError("To child for this, go cry to your mom")
        return func(user)
    return wrapper


@adult_only
def show_user(user):
    print("Access granted, use it wisely! Age:", user.age)


birthday = input("Enter your birth date (dd/mm/yyyy): ")
user = User(birthday)
show_user(user)

try:
    birthday = input("Enter your birth date (dd/mm/yyyy): ")
    user = User(birthday)
    show_user(user)
except ValueError as error:
    print("Error:", error)
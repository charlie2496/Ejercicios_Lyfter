class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            raise ValueError("Withdrawal amount must be positive and cannot exceed the current balance.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, min_balance=0, balance=0):
        if min_balance < 0:
            raise ValueError("Minimum balance cannot be negative.")

        if balance < min_balance:
            raise ValueError("Initial balance cannot be less than the minimum balance.")
        super().__init__(account_number, account_holder, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= self.min_balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            raise ValueError("Withdrawal amount must be positive and maintain the minimum balance.")


account1=SavingsAccount("123456", "John Doe", min_balance=100, balance=500)
print(initial_balance := account1.get_balance())


account1.withdraw(400)
print("Final balance:", account1.get_balance())

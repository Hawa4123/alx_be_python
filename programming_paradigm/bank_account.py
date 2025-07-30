import os

class BankAccount:
    BALANCE_FILE = "balance.txt"

    def __init__(self, initial_balance=0):
        self.__account_balance = self._load_balance(initial_balance)

    def _load_balance(self, default_balance):
        if os.path.exists(self.BALANCE_FILE):
            with open(self.BALANCE_FILE, "r") as file:
                return float(file.read())
        return default_balance

    def _save_balance(self):
        with open(self.BALANCE_FILE, "w") as file:
            file.write(str(self.__account_balance))

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            self._save_balance()
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            self._save_balance()
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")
import os

class BankAccount:
    BALANCE_FILE = "balance.txt"

    def __init__(self, initial_balance=250):
        
        self.__account_balance = initial_balance
        self._save_balance()

    def _save_balance(self):
        with open(self.BALANCE_FILE, "w") as file:
            file.write(f"{self.__account_balance:.2f}")

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
        print(f"Current Balance: ${self.__account_balance:.2f}")

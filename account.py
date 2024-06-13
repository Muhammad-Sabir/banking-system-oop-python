class Account():
    def __init__(self,  account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account Number: {self.account_number} \nAccount Holder: {self.account_holder} \nBalance: ${self.balance:.2f}"
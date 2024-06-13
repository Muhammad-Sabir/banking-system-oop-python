from account import Account

class Bank():
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if(account.account_number == account_number):
                return account
        return None

    def list_accounts(self):
        for account in self.accounts:
            # calling __str__ of the Account class
            print(account)
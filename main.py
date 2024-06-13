from account import Account
from bank import Bank

def main():
    bank = Bank()

    while True:
        print("\n--Banking System--")
        print("1. Create an Account")
        print("2. Find an Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. List All Accounts")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit (if any or just write 0): "))
            account = Account(account_number, account_holder, initial_deposit)
            bank.add_account(account)
            print("Account added successfully.")

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                print(account)
            else:
                print("Account not found.")
        
        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                if account.deposit(amount):
                    print("Deposit successful.")
                else:
                    print("Invalid deposit amount.")
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Invalid withdrawal amount or insufficient balance.")
            else:
                print("Account not found.")

        elif choice == "5":
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                print(f"Current balance: Rs.{account.get_balance():.2f}")
            else:
                print("Account not found.")

        elif choice == "6":
            print("\nAll accounts in the bank:")
            bank.list_accounts()

        elif choice == "7":
            print("Exiting the banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
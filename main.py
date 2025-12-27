from account import Account
from bank import Bank

def main():
    bank = Bank()
    
# User creation
    
    while True:
        print("\n1. Create User")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            name = input("Enter name: ").lower()
            pin = int(input("Set PIN: "))
            bank.create_user(name, pin)
            
        elif choice == '2':
            name = input("Name: ").lower()
            pin = int(input("PIN: "))
            
            user = bank.authenticate_user(name, pin)
            if user:
                print(f"Welcome, {user.name}!")
                break
            else:
                print("Invalid credentials")
                
        elif choice == '3':
            exit()
        
# Account creation

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Logout")

        choice = input("Choice: ")
        
        if choice == '1':
            bank.create_account(user.name)
                
        elif choice == '2':
            try:
                account_number = int(input("Account number: "))
                amount = int(input("Enter Amount to deposit: "))
                bank.deposit(account_number, amount)
            except ValueError:
                print("Invalid input")
                
        elif choice == '3':
            try:
                account_number = int(input("Account number: "))
                amount = int(input("Enter Amount to withdraw: "))
                bank.withdraw(account_number, amount)
            except ValueError:
                print("Invalid input")
                
        elif choice == '4':
            try:
                account_number = int(input("Account number: "))
                bank.check_balance(account_number)
            except ValueError:
                print("Invalid input")
                
        elif choice == '5':
            try:
                account_number = int(input("Account number: "))
                bank.show_transactions(account_number)
            except ValueError:
                print("Invalid input")       
                 
        elif choice == '6':   
            print("Logged out!")
            break
        
        else:
            print("Invalid choice")
            
main()
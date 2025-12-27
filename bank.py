from user import User
from database import Database
from account import Account
from transaction import Transaction
import sqlite3

class Bank:
    def __init__(self,):
        self.db = Database()

# USER         
    def create_user(self, name, pin):
        try:
            self.db.cursor.execute(
            "INSERT INTO users (name, pin) VALUES (?, ?)",
            (name, pin)
            )
            self.db.conn.commit()
            print("User created successfully")
        except sqlite3.IntegrityError:
            print("User already exists")
    
    def authenticate_user(self, name, pin):
        self.db.cursor.execute(
            "SELECT name, pin FROM users WHERE name=? AND pin=?",
            (name, pin)
        )
        row = self.db.cursor.fetchone()

        if row:
            return User(row[0], row[1])
        return None
    
# ACCOUNT
    def create_account(self, user_name):
        try:
            self.db.cursor.execute(
                "INSERT INTO accounts (owner, balance) VALUES (?, ?)",
                (user_name, 0)
            )
            self.db.conn.commit()
            
            account_number = self.db.cursor.lastrowid
            print("Account created successfully")
            print(f"Your account number is: {account_number}")
        except sqlite3.Error as e:
            print("Failed to create account:", e)
            
    def get_account(self, account_number):
        self.db.cursor.execute(
            "SELECT account_number, owner, balance FROM accounts WHERE account_number=?",
            (account_number,)
        )
        row = self.db.cursor.fetchone()
        if row:
            account_number, owner, balance = row
            account = Account(account_number, owner)
            account.balance = balance 
            return account
        
        return None
    
    def check_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"Balance: {account.balance}")
        else:
            print("Account not found!")
# Update account with DB
    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if not account:
            print("Account not found!")
            return
        
        print(account.deposit(amount, self.db))

        
    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if not account:
            print("Account not found!")
            return
        
        print(account.withdraw(amount, self.db))     
    
    def show_transactions(self, account_number):
        self.db.cursor.execute(
            """SELECT 
                    type, 
                    amount, 
                    balance_after, 
                    strftime('%Y-%M-%d %H:%M:%S', timestamp) 
                    FROM transactions 
                    WHERE account_number=?
            """, (account_number,))
        
        rows = self.db.cursor.fetchall()
        
        if not rows:
            print("No transactions found")
            return
        
        for row in rows:
            print(row)
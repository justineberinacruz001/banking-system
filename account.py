from transaction import Transaction
import datetime

class Account:
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0
        self.timestamp = datetime.datetime.now()
        
        
    def deposit(self, amount, db):
        if amount <= 0:
            return "Enter a positive amount"

        self.balance += amount
        
        # UPDATE BALANCE
        db.cursor.execute(
            "UPDATE accounts SET balance=? WHERE account_number=?",
            (self.balance, self.account_number)
        )
        
        db.cursor.execute(
            """
            INSERT INTO transactions (account_number, type, amount, balance_after, timestamp)
            VALUES (?, ?, ?, ?, ?)
            """,
            (self.account_number, "DEPOSIT", amount, self.balance, self.timestamp)
        )
        
        db.conn.commit()
        return "Deposit successful"
    
    def withdraw(self, amount, db):
        if amount <= 0:
            return "Enter a positive amount"
        if amount > self.balance:
            return "Insufficient balance"
        
        self.balance -= amount

        db.cursor.execute(
            "UPDATE accounts SET balance=? WHERE account_number=?",
            (self.balance, self.account_number)
        )
        
        db.cursor.execute(
            """
            INSERT INTO transactions (account_number, type, amount, balance_after, timestamp)
            VALUES(?, ?, ?, ?, ?)
            """,
            (self.account_number, "WITHDRAW", amount, self.balance, self.timestamp)
        )
        
        db.conn.commit()
        return "Withdraw successful"

    
    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return

        for t in self.transactions:
            print(t)
import datetime

class Transaction:
    def __init__(self, transaction_type, amount, balance_after):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.datetime.now().strftime("$Y-%m-%d %H:%M:%S")
        
    def __str__(self):
        return(
            f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | "
            f"{self.transaction_type} | "
            f"Amount: {self.amount} | "
            f"Balance: {self.balance_after}"
        )
        
    def save(self, db, account_number):
        db.cursor.execute("""
        INSERT INTO transactions
        (account_number, type, amount, balance_after, timestamp)
        VALUES(?, ?, ?, ?, ?)
        """,(
            account_number,
            self.amount,
            self.balance_after,
            self.timestamp
        ))
        db.conn.commit()
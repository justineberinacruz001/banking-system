import sqlite3 

class Database:
    def __init__(self, db_name="bank.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            pin INTEGER
        )
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number INTEGER PRIMARY KEY AUTOINCREMENT,
            owner TEXT,
            balance INTEGER
        )
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number INTEGER,
            type TEXT,
            amount INTEGER,
            balance_after INTEGER,
            timestamp TEXT
        )
        """)
        
        self.conn.commit()
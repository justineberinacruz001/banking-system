# 🏦 Banking System (Python, OOP, SQLite)

A simple **console-based banking system** built with **Python**, following **Object-Oriented Programming (OOP)** principles and using **SQLite** for persistent data storage.

This project demonstrates user authentication, account management, balance updates, and transaction history — suitable for learning purposes and as a **portfolio project**.

---

## ✨ Features

- User registration and login (PIN-based authentication)
- Create bank accounts (auto-generated account numbers)
- Deposit and withdraw money
- Check account balance
- View transaction history
- Persistent storage using SQLite
- Clean OOP design (Bank, User, Account, Transaction, Database)

---

## 🛠 Technologies Used

- **Python 3**
- **SQLite3** (built-in Python library)
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```
banking_system/
│
├── main.py          # Entry point (CLI menu)
├── bank.py          # Bank logic (users, accounts, operations)
├── account.py       # Account behavior (deposit, withdraw)
├── user.py          # User model
├── transaction.py   # Transaction model
├── database.py      # SQLite database connection & setup
├── banking.db       # SQLite database (auto-created)
└── README.md
```

---

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/justineberinacruz001/banking-system.git
cd banking-system
```

2. **Run the program**

```bash
python main.py
```

> ⚠️ Make sure you have **Python 3.8+** installed.

---

## 🧭 Program Flow

1. Create a user
2. Login using name and PIN
3. Create a bank account (account number is generated automatically)
4. Perform banking operations:
   - Deposit
   - Withdraw
   - Check balance
   - View transaction history
5. Logout

---

## 📸 Sample Output

```
Welcome, justine!

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Logout

Account created successfully
Your account number is: 1

Deposit successful
Withdrawal successful

('DEPOSIT', 500, 500, '2025-01-10 14:22:01')
('WITHDRAW', 200, 300, '2025-01-10 14:23:11')
```

---

## 🧠 What I Learned

- Applying OOP concepts in a real project
- Separating concerns between logic, data, and UI
- Working with SQLite databases in Python
- Handling user input and errors cleanly
- Designing a simple but realistic banking workflow

---

## 📌 Possible Improvements

- Password hashing instead of plain PIN storage
- Multiple accounts per user
- Admin features
- GUI or Web interface
- Unit testing

---

## 👤 Author

**Justine Cruz**\
GitHub: [https://github.com/justineberinacruz001](https://github.com/justineberinacruz001)

---

## 📄 License

This project is for educational purposes.


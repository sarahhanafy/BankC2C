import sqlite3

# Function to create a new account
def create_account(account_number, pin, account_type):
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO users (account_number, pin, account_type)
    VALUES (?, ?, ?)
    ''', (account_number, pin, account_type))

    # Get the user_id of the newly created user
    user_id = cursor.lastrowid

    cursor.execute('''
    INSERT INTO accounts (user_id, balance)
    VALUES (?, ?)
    ''', (user_id, 0))

    conn.commit()
    conn.close()

    return user_id

# Function to check account balance
def check_balance(account_number):
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT balance FROM accounts
    INNER JOIN users ON accounts.user_id = users.user_id
    WHERE users.account_number = ?
    ''', (account_number,))

    balance = cursor.fetchone()[0]

    conn.close()

    return balance

# Function to make a deposit
def deposit(account_number, amount):
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE accounts
    SET balance = balance + ?
    WHERE user_id = (
        SELECT user_id FROM users WHERE account_number = ?
    )
    ''', (amount, account_number))

    conn.commit()
    conn.close()

# Function to make a withdrawal
def withdraw(account_number, amount):
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE accounts
    SET balance = balance - ?
    WHERE user_id = (
        SELECT user_id FROM users WHERE account_number = ?
    )
    ''', (amount, account_number))

    conn.commit()
    conn.close()

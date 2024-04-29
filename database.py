import sqlite3

# Function to create the SQLite database and tables
def create_database():
    # Connect to the SQLite database (creates a new database if not exists)
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        account_number TEXT UNIQUE NOT NULL,
        pin TEXT NOT NULL,
        account_type TEXT NOT NULL
    )
    ''')

    # Create accounts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        balance REAL NOT NULL DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the database when this module is executed
if __name__ == '__main__':
    create_database()

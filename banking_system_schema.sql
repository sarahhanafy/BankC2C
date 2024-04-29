-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    account_number TEXT UNIQUE NOT NULL,
    pin TEXT NOT NULL,
    account_type TEXT NOT NULL
);

-- Create the accounts table
CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    balance REAL NOT NULL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert initial data (admin and customer accounts) for testing purposes
INSERT INTO users (account_number, pin, account_type) VALUES ('admin123', '1234', 'admin');
INSERT INTO users (account_number, pin, account_type) VALUES ('customer456', '4321', 'customer');

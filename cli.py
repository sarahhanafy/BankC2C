import banking_functions

# Function to display menu options
def display_menu():
    print("\nWelcome to the Banking System")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

# Main function to run the CLI
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account_type = input("Enter account type (e.g., customer, admin): ")
            user_id = banking_functions.create_account(account_number, pin, account_type)
            print("Account created successfully! User ID:", user_id)

        elif choice == '2':
            account_number = input("Enter account number: ")
            balance = banking_functions.check_balance(account_number)
            print("Balance:", balance)

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            banking_functions.deposit(account_number, amount)
            print("Deposit successful!")

        elif choice == '4':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            banking_functions.withdraw(account_number, amount)
            print("Withdrawal successful!")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

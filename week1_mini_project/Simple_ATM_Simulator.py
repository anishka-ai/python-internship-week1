
# Mini Project: Simple ATM Simulator
# Week 1 Internship Project

# Initial account details
CORRECT_PIN = "1234"
balance = 5000.00


def login():
    """Verify the user's PIN."""
    print("===== Welcome to Simple ATM =====")

    for attempt in range(3):
        pin = input("Enter your 4-digit PIN: ")

        if pin == CORRECT_PIN:
            print("\nLogin successful!")
            return True

        remaining = 2 - attempt

        if remaining > 0:
            print(f"Incorrect PIN! Attempts remaining: {remaining}")
        else:
            print("Too many incorrect attempts. Access denied.")

    return False


def check_balance():
    """Display the current account balance."""
    print(f"\nYour current balance is: Rs. {balance:.2f}")


def deposit():
    """Deposit money into the account."""
    global balance

    try:
        amount = float(input("Enter amount to deposit: Rs. "))

        if amount <= 0:
            print("Error: Deposit amount must be positive.")
        else:
            balance += amount
            print(f"Rs. {amount:.2f} deposited successfully!")
            print(f"Updated balance: Rs. {balance:.2f}")

    except ValueError:
        print("Invalid input! Please enter a valid amount.")


def withdraw():
    """Withdraw money if sufficient balance is available."""
    global balance

    try:
        amount = float(input("Enter amount to withdraw: Rs. "))

        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Please collect your cash: Rs. {amount:.2f}")
            print(f"Remaining balance: Rs. {balance:.2f}")

    except ValueError:
        print("Invalid input! Please enter a valid amount.")


def main():
    """Run the ATM application."""
    if not login():
        return

    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("==============================")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using Simple ATM!")
            print("Have a nice day!")
            break

        else:
            print("Invalid choice! Please select between 1 and 4.")


if __name__ == "__main__":
    main()

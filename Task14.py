"""ATM Management System

Create a Python program that simulates a simple ATM. The user should be able to check balance, deposit money, withdraw money, and exit."""


# Task 13: ATM Management System

balance = 5000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your current balance is: ₹", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: ₹"))

        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("New balance: ₹", balance)
        else:
            print("Invalid amount!")

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Invalid amount!")

        elif amount > balance:
            print("Insufficient balance!")

        else:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance: ₹", balance)

    elif choice == 4:
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please try again.")
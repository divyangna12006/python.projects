expenses = []

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append([item, amount])
        print("Expense added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for item, amount in expenses:
                print(f"{item}: ₹{amount}")

    elif choice == "3":
        total = 0
        for item, amount in expenses:
            total += amount
        print("Total Expenses = ₹", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
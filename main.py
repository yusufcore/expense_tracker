expenses = []

while(True):
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Your Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        description = input("Description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

    elif choice == "2":
        for expense in expenses:
            print(expense)
    
    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Spent: ${total}")
    
    elif choice == "4":
        break
    else:
        print("Invalid Choice")
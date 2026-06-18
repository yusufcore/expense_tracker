from expense import Expense
import datetime
import calendar

def main():
    print(f"Running Expense Tracker!") 
    expense_file_path = "expense.csv"
    budget = 2000

    # Get user to input their expenses.
    expense = get_user_expense()

    # then write their expense to a file.
    save_expense(expense, expense_file_path)
    # read the file and summarize all the expenses.
    summarize_expense(expense_file_path, budget)

    # pass --> Its a keyword in Python. pass is used when their is no code inside the functions created.

def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))
    print(f"You entered {expense_name}, {expense_amount}")

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "fun",
        "Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}, {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input("Enter your Preference {value_range}:")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount= expense_amount 
                )
            return new_expense
        else:
            print("Invalid Input")

        break

    

def save_expense(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a" ) as f:
         f.write(f"{expense.name}, {expense.amount},{expense.category}\n")
    

def summarize_expense(expense_file_path, budget):
    print(f"Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")

            line_expense = Expense(
                name=expense_name, 
                amount= float(expense_amount), 
                category=expense_category
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expense by category:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")   
    

    total_spent = sum(ex.amount for ex in expenses)
    print(f"Total Spent: ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"Budget remaining ${remaining_budget:.2f}")

    # Get the current date
    now = datetime.datetime.now()

    # Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day

    print("Remaining days in the current month:", remaining_days)

    daily_budget = remaining_budget / remaining_days

    print(f" Budget Per Day: ${daily_budget:.2f}")



if __name__ == "__main__":
    main()
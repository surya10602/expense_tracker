import json
from datetime import datetime
DATA_FILE = "expense.json"
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"expenses": [], "savings_goal": 0, "saved": 0}
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
def add_expense():
    data = load_data()
    amount = float(input("Enter expense amount: ₹ "))
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    date = datetime.now()
    data["expenses"].append({"amount": amount, "category": category, "date": date})
    save_data(dat)
    print("\nExpense added successfully!\n")
def view_expense():
    data = load_data()
    if not data["expenses"]:
        print("\nNo expenses recorded yet.\n")
        return
    print("\nExpense Records:")
    for exp in data["expenses"]:
        print(f"- ₹{exp['amount']} | {exp['category']} | {exp['date']}")
    print()
def view_summary():
    data = load_data()
    summary = {}
    for exp in data["expenses"]:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]
    print("\nSpending Summary by Category:")
    for category, amount in summary.item():
        print(f"- {category}: ₹{amount}")
    print()
def set_savings_goal():
    data = load_data()
    goal = float(input("Enter your savings goal: ₹ "))
    data["saving_goal"] = goal
    save_data(data)
    print("\nSavings goal updated!\n")
def savings_progress():
    data = load_data()
    total_spent = sum(exp["amount"] for exp in data["expenses"])
    saved = data["saving_goal"] - total_spent if data["savings_goal"] > 0 else 0
    print("\nSavings Progress:")
    print(f"Savings Goal: ₹{data['savings_goal']}")
    print(f"Total Spent: ₹{total_spent}")
    print(f"Remaining to Save: ₹{saved if saved > 0 else 0}\n")
def menu():
    while True:
        print("====== Expense & Savings Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Set Savings Goal")
        print("5. View Savings Progress")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            set_savings_goal()
        elif choice == '5':
            savings_progress()
        elif choice == '6':
            print("\nThank you for using Expense Tracker!")
            break
        else:
            print("\nInvalid choice! Please try again.\n")
if __name__ == "__main__":
    menu()

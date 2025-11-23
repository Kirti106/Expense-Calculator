import csv
import datetime
import os

EXPENSEFILE = 'expenses.csv'
CSVHEADERS = ['Date', 'Category', 'Amount']

def init():
    if not os.path.exists(EXPENSEFILE):
        print(f"Creating new data file: {EXPENSEFILE}")
        try:
            f=open(EXPENSEFILE, 'w', newline='', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow(CSVHEADERS)
        except Exception as e:
            print(f"Error initializing file: {e}")

def lexp():
    expenses = []
    if not os.path.exists(EXPENSEFILE):
        return expenses
    try:
        f=open(EXPENSEFILE, 'r', newline='', encoding='utf-8')
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row['Amount'] = float(row['Amount'])
                expenses.append(row)
            except ValueError:
                print(f"Skipping row with invalid amount: {row}")
                continue
    except Exception as e:
        print(f"Error loading expenses: {e}")
    return expenses

def addexp():
    print("\n--- Add New Expense ---")
    while True:
        date_str = input("Enter date (YYYY-MM-DD, leave blank for today): ").strip()
        if not date_str:
            date_str = datetime.date.today().strftime('%Y-%m-%d')
            break
        try:
            datetime.date.fromisoformat(date_str)
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    category = input("Enter category (e.g., Food, Transport, Rent): ").strip().capitalize()
    if not category:
        category = "Miscellaneous"
    while True:
        try:
            amount_str = input("Enter amount: ").strip()
            amount = round(float(amount_str), 2)
            if amount <= 0:
                print("Amount must be positive.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")    
    new_expense = {
        'Date': date_str,
        'Category': category,
        'Amount': amount
    }
    try:
        f=open(EXPENSEFILE, 'a', newline='', encoding='utf-8')
        writer = csv.DictWriter(f, fieldnames=CSVHEADERS)
        writer.writerow(new_expense)
        print(f"\n Expense added: {date_str} - {category} - ${amount:.2f}")
    except Exception as e:
        print(f"Error writing expense to file: {e}")

def summary(expenses):
    if not expenses:
        print("\n No expenses recorded yet. Add some expenses first!")
        return
    print("\n--- Expense Summary ---")
    total_spending = sum(expense['Amount'] for expense in expenses)
    print(f" Total Recorded Spending: ${total_spending:.2f}\n")
    category_totals = {}
    for expense in expenses:
        category = expense['Category']
        amount = expense['Amount']
        category_totals[category] = category_totals.get(category, 0) + amount
    print(" Spending Breakdown by Category:")
    sorted_categories = sorted(category_totals.items(), key=lambda item: item[1], reverse=True)
    for category, total in sorted_categories:
        percentage = (total / total_spending) * 100
        print(f"- {category: <15}: ${total: >8.2f} ({percentage:.1f}%)")

def main():
    init()
    while True:
        print("\n" + "="*30)
        print("PYTHON SIMPLE BUDGET TRACKER")
        print("="*30)
        print("1. Add New Expense")
        print("2. Show Expense Summary")
        print("3. Exit")
        print("-" * 30)
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        if choice == '1':
            addexp()
        elif choice == '2':
            expenses = lexp()
            summary(expenses)
        elif choice == '3':
            print("\nThank you for using the Budget Tracker! Goodbye.")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
main()
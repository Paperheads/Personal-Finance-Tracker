from repository.tracker import TransactionService
from services.file_repo import TransactionRepository
from models.transaction import Transaction, TransactionFormatter
from datetime import datetime

FILE_PATH = './services/package.json'

def input_int_value(label):
    while True:
        try:
            return int(input(f"Enter integer: {label}: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_str_value(label):
    return input(f"Enter text: {label}: ")

def show_menu():
    print("""
1 - Add income
2 - Add expense
3 - Show balance
4 - Show all transactions
5 - Show only income
6 - Show only expenses
7 - Sort by amount
8 - Sort by date
9 - Exit
""")

def handle_add_income(user):
    amount = input_int_value("Amount")
    description = input_str_value("Description")
    category = input_str_value("Category")
    tx = Transaction(amount, 'income', description, datetime.now(), category)
    tx.write_to_file()
    user._TransactionService__balance += amount
    print("Income added.")

def handle_add_expense(user):
    amount = input_int_value("Amount")
    if amount > user.balance:
        print("Not enough balance!")
        return
    description = input_str_value("Description")
    category = input_str_value("Category")
    tx = Transaction(amount, 'expense', description, datetime.now(), category)
    tx.write_to_file()
    user._TransactionService__balance -= amount
    print("Expense recorded.")

def handle_show_balance(user):
    print(f"{user.name}, your current balance is: {user.balance}")

def handle_show_all():
    txs = TransactionRepository.get_all(FILE_PATH)
    TransactionFormatter.print_transactions(txs)

def handle_show_income():
    txs = TransactionRepository.filter_by_type(FILE_PATH, 'income')
    TransactionFormatter.print_transactions(txs)

def handle_show_expense():
    txs = TransactionRepository.filter_by_type(FILE_PATH, 'expense')
    TransactionFormatter.print_transactions(txs)

def handle_sort_by_amount():
    txs = TransactionRepository.sort_by_amount(FILE_PATH, ascending=True)
    TransactionFormatter.print_transactions(txs)

def handle_sort_by_date():
    txs = TransactionRepository.sort_by_date(FILE_PATH, ascending=False)
    TransactionFormatter.print_transactions(txs)

def launch_app():
    name = input_str_value('Your name')
    balance = input_int_value('Initial balance')
    user = TransactionService(name, balance)

    actions = {
        "1": lambda: handle_add_income(user),
        "2": lambda: handle_add_expense(user),
        "3": lambda: handle_show_balance(user),
        "4": handle_show_all,
        "5": handle_show_income,
        "6": handle_show_expense,
        "7": handle_sort_by_amount,
        "8": handle_sort_by_date,
        "9": lambda: print("Goodbye!")
    }

    while True:
        show_menu()
        choice = input("Choose action: ")

        if choice == "9":
            actions[choice]()
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Try again.")
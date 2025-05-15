from repository.tracker import TransactionService
from services.file_repo import TransactionRepository
from models.transaction import Transaction, TransactionFormatter
from datetime import datetime


FILE_PATH = './services/package.json'  # можно использовать абсолютный путь, если хочешь


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


def launch_app():
    name = input_str_value('Your name')
    balance = input_int_value('Initial balance')
    user = TransactionService(name, balance)

    while True:
        show_menu()
        choice = input("Choose action: ")

        if choice == "1":
            amount = input_int_value("Amount")
            description = input_str_value("Description")
            category = input_str_value("Category")
            tx = Transaction(amount, 'income', description, datetime.now(), category)
            tx.write_to_file()
            user._TransactionService__balance += amount
            print("Income added.")

        elif choice == "2":
            amount = input_int_value("Amount")
            if amount > user.balance:
                print("Not enough balance!")
                continue
            description = input_str_value("Description")
            category = input_str_value("Category")
            tx = Transaction(amount, 'expense', description, datetime.now(), category)
            tx.write_to_file()
            user._TransactionService__balance -= amount
            print("Expense recorded.")

        elif choice == "3":
            print(f"{user.name}, your current balance is: {user.balance}")

        elif choice == "4":
            txs = TransactionRepository.get_all(FILE_PATH)
            TransactionFormatter.print_transactions(txs)

        elif choice == "5":
            txs = TransactionRepository.filter_by_type(FILE_PATH, 'income')
            TransactionFormatter.print_transactions(txs)

        elif choice == "6":
            txs = TransactionRepository.filter_by_type(FILE_PATH, 'expense')
            TransactionFormatter.print_transactions(txs)

        elif choice == "7":
            txs = TransactionRepository.sort_by_amount(FILE_PATH, ascending=True)
            TransactionFormatter.print_transactions(txs)

        elif choice == "8":
            txs = TransactionRepository.sort_by_date(FILE_PATH, ascending=False)
            TransactionFormatter.print_transactions(txs)

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
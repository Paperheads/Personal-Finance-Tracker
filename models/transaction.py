from datetime import datetime

from services.file_repo import TransactionRepository


class Transaction:

    def __init__(self, amount : int, type_of : str,
                 description : str = None, date : datetime = datetime.now(), category : str = None):

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if type_of not in ["income", "expense"]:
            raise ValueError("Type of must be either income or expense")
        self.type_of = type_of
        self.amount = amount
        self.date = date

        self.description = description
        self.category = category


    def get_data(self):
        return {
            "amount": self.amount,
            "type_of": self.type_of,
            "description": self.description,
            "date": self.date,
            "category": self.category,
        }

    def write_to_file(self):
        content = TransactionRepository.read('/Users/davyd/Desktop/Learning/Python_learning/Personal Finance Tracker/services/package.json')
        additional_content = Transaction.get_data(self)

        TransactionRepository.write('/Users/davyd/Desktop/Learning/Python_learning/Personal Finance Tracker/services/package.json', content, additional_content)


class TransactionFormatter:
    @staticmethod
    def print_transactions(transactions):
        for t in transactions:
            print(f"{t['date'].strftime('%Y-%m-%d %H:%M')} | {t['type_of'].upper():7} | {t['amount']:>6} | {t['category'] or 'No category'} | {t['description'] or 'No description'}")
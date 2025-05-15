import json
from datetime import datetime


class TransactionRepository:

    @staticmethod
    def read(file_name):
        try:
            with open(file_name, 'r') as file:
                content = file.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def write(file_name, content, additional_content):
        content.append(additional_content)
        with open(file_name, 'w') as file:
            json.dump(content, file, indent=2, default=str)

    @staticmethod
    def parse_date_safe(date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_all(file_name):
        content = TransactionRepository.read(file_name)
        for item in content:
            item["date"] = TransactionRepository.parse_date_safe(item["date"])
        return content

    @staticmethod
    def sort_by_amount(file_name, ascending=True):
        txs = TransactionRepository.get_all(file_name)
        return sorted(txs, key=lambda x: x["amount"], reverse=not ascending)

    @staticmethod
    def sort_by_date(file_name, ascending=True):
        txs = TransactionRepository.get_all(file_name)
        return sorted(txs, key=lambda x: x["date"], reverse=not ascending)

    @staticmethod
    def sort_by_category(file_name):
        txs = TransactionRepository.get_all(file_name)
        return sorted(txs, key=lambda x: (x["category"] or "").lower())

    @staticmethod
    def filter_by_type(file_name, type_of):
        txs = TransactionRepository.get_all(file_name)
        return [t for t in txs if t["type_of"] == type_of]

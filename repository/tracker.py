

class TransactionService:

    def __init__(self, name, balance : int = 0):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if int(value, int) and value > 0:
            self.__balance = value
        else:
            raise ValueError("Balance must be positive and integer value")

    def __str__(self):
        return f"{self.name} balance: {self.__balance}"

    def __eq__(self, other):
        return self.__balance == other.__balance

    def __lt__(self, other):
        return self.__balance < other.__balance

    def __gt__(self, other):
        return self.__balance > other.__balance


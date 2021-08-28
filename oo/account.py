from datetime import date

class Customer:

    def __init__(self, first_name, last_name, doc_number):
        self.first_name = first_name
        self.last_name = last_name
        self.doc_number = doc_number
class Account:

    __accounts_qtd = 0

    def __init__(self, number, customer, balance, limit=1000.0):
        self.__number = number
        self.__owner = customer # aggregation (Account have one Customer - Customer exists even if Account doesn't )
        self.__balance = balance
        self._limit = limit
        self.__history = History()
        Account.__accounts_qtd += 1 # composition (Account have History - History exists only if account exists)

    @staticmethod
    def get_accounts_qtd():
        return Account.__accounts_qtd

    def deposit(self, value):
        self.__history.transactions.append("deposit {}".format(value))
        self.__balance += value

    def withdraw(self, value):
        if (self.__balance < value):
            return False
        self.__balance -= value
        self.__history.transactions.append("withdraw {}".format(value))
        return True

    def transfer_to(self, destination, value):
        if (self.withdraw(value)):
            self.__history.transactions.append("transfer {} to account {}".format(value, destination.get_number))
            destination.deposit(value)
            return True
        return False

    def extract(self):
        self.__history.transactions.append("get extract with {} balance".format(self.__balance))
        print("number: {} \nowner: {} \nbalance: {}".format(self.__number, self.__owner.first_name, self.__balance))

    def get_number(self):
        return self.__number

    def get_history(self):
        return self.__history

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        if (limit > 10000.0):
            print('wrong limit')
        else:
            self._limit = limit

class History:

    def __init__(self):
        self.open_date = date.today()
        self.transactions = []

    def print(self):
        print("open date: {}".format(self.open_date))
        print("transactions: ")
        for t in self.transactions:
            print("-", t)
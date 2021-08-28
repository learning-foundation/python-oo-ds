from datetime import date

class Customer:

    def __init__(self, first_name, last_name, doc_number):
        self.first_name = first_name
        self.last_name = last_name
        self.doc_number = doc_number
class Account:

    __accounts_qtd = 0

    def __init__(self, number, customer, balance, limit=1000.0):
        self.number = number
        self.owner = customer # aggregation (Account have one Customer - Customer exists even if Account doesn't )
        self.balance = balance
        self.limit = limit
        self.history = History()
        Account.__accounts_qtd += 1 # composition (Account have History - History exists only if account exists)

    @staticmethod
    def get_accounts_qtd():
        return Account.__accounts_qtd

    def deposit(self, value):
        self.history.transactions.append("deposit {}".format(value))
        self.balance += value

    def withdraw(self, value):
        if (self.balance < value):
            return False
        self.balance -= value
        self.history.transactions.append("withdraw {}".format(value))
        return True

    def transfer_to(self, destination, value):
        if (self.withdraw(value)):
            self.history.transactions.append("transfer {} to account {}".format(value, destination.number))
            destination.deposit(value)
            return True
        return False

    def extract(self):
        self.history.transactions.append("get extract with {} balance".format(self.balance))
        print("number: {} \nowner: {} \nbalance: {}".format(self.number, self.owner.first_name, self.balance))

class History:

    def __init__(self):
        self.open_date = date.today()
        self.transactions = []

    def print(self):
        print("open date: {}".format(self.open_date))
        print("transactions: ")
        for t in self.transactions:
            print("-", t)
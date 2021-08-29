from datetime import date

class History:

    def __init__(self):
        self.open_date = date.today()
        self.transactions = []

    def print(self):
        print("open date: {}".format(self.open_date))
        print("transactions: ")
        for t in self.transactions:
            print("-", t)
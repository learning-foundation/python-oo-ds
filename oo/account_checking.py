from account import Account

class AccountChecking(Account):
    
    def __init__(self, number, customer, balance, limit=1000.0):
        super().__init__(number, customer, balance, 'Checking', limit)

    def update(self, tax):
        self._balance += self._balance * tax * 2
        return self._balance

    def deposit(self, value):
        self._balance += value - 0.10
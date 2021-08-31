from account import Account

class AccountInvestment(Account):
    def __init__(self, number, customer, balance, limit=1000.0):
        super().__init__(number, customer, balance, 'Investment', limit)

    def update(self, tax):
        self._balance += self._balance * tax * 5
        return self._balance

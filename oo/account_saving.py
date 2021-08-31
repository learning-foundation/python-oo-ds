from account import Account

class AccountSaving(Account):

    def __init__(self, number, customer, balance, limit=1000.0):
        super().__init__(number, customer, balance, 'Saving', limit)
    
    def update(self, tax):
        self._balance += self._balance * tax * 3
        return self._balance
from account import Account

class AccountUpdater:
    
    def __init__(self, selic, total_balance=0):
        self._selic = selic
        self._total_balance = total_balance

    def execute(self, account):
        print("Balance: {}".format(account.balance))
        self._total_balance += account.update(self._selic)
        print("Final Balance: {}".format(self._total_balance))

    @property
    def total_balance(self):
        return self._total_balance
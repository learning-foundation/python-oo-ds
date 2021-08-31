from account_updater import AccountUpdater
from account_checking import AccountChecking
from account_saving import AccountSaving
from account import Account
from customer import Customer
from manager import Manager
from director import Director

customer1 = Customer('John', 'Oliver', '001002')
customer2 = Customer('Naty', 'Queen', '990123')

account1 = Account('123-4', customer1, 1000.0)
account2 = Account('000-1', customer2, 1000.0)

account2.extract()
account2.deposit(100.0)
account2.withdraw(50.0)
account2.transfer_to(account1, 200.0)
account2.extract()
account2.get_history().print()

account1.get_history().print()

print('Accounts qtd {}'.format(Account.get_accounts_qtd()))

account1.limit = 10001.0
print(account1.id)
print(account2.id)

manager = Manager('Carl', '889889', 1000.0, '123456', 0)
print(manager.get_bonus())
print(vars(manager))

account = Account('222-4', customer1, 1000.0)
ac = AccountChecking('222-5', customer1, 1000.0)
av = AccountSaving('222-5', customer1, 1000.0)

account.update(0.01)
ac.update(0.01)
av.update(0.01)

print(account.balance)
print(ac.balance)
print(av.balance)
print(ac)

aud = AccountUpdater(0.01)

aud.execute(account)
aud.execute(ac)
aud.execute(av)

print('Total balance: {}'.format(aud.total_balance))

e = Director('Rose', '111222', 100.5)
from account import Account, Customer

customer1 = Customer('John', 'Oliver', '001002')
customer2 = Customer('Naty', 'Queen', '990123')

account1 = Account('123-4', customer1, 1000.0)
account2 = Account('000-1', customer2, 1000.0)

account2.extract()
account2.deposit(100.0)
account2.withdraw(50.0)
account2.transfer_to(account1, 200.0)
account2.extract()
account2.history.print()

account1.history.print()
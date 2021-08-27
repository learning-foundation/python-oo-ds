def create_account(number, owner, balance, limit):
    account = {'number': number, 'owner': owner, 'balance': balance, 'limit': limit}
    return account

def deposit(account, value):
    account['balance'] += value

def withdraw(account, value):
    account['balance'] -= value

def extract(account):
    print('number: {} \nbalance: {}'.format(account['number'], account['balance']))

account = create_account('123-7', 'John', 500.0, 1000.0)
deposit(account, 50.0)
extract(account)

withdraw(account, 20.0)
extract(account)
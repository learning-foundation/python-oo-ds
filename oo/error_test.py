from account_checking import AccountChecking

def method1():
    print('method1 starts')
    method2()
    print('method1 ends')

def method2():
    print('method2 starts')
    ac = AccountChecking('111-1', 'Rose', 0)
    for i in range(1, 15):
        ac.deposit(i + 1000)
        print(ac.balance)
        if (i == 5):
            ac = None

    print('method2 ends')

if __name__ == '__main__':
    print('main starts')
    try:
        method1()
    except:
        print('raise error')
    print('main ends')
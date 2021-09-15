class TaxableManipulator:
    
    def tax_calc(self, taxable_list):
        total = 0
        for t in taxable_list:
            total += t.get_tax_value()

        return total


if __name__=='__main__':
    from account_checking import AccountChecking
    from life_insurance import LifeInsurance

    ac1 = AccountChecking('111-1', 'John', 1000.0) # 10.0
    ac2 = AccountChecking('111-2', 'Victor', 2000.0) # 20.0
    li1 = LifeInsurance(100.0, 'John', '00-111') # 55
    li2 = LifeInsurance(200.0, 'Mary', '00-112') # 60

    taxable_list = []

    taxable_list.append(ac1)
    taxable_list.append(ac2)
    taxable_list.append(li1)
    taxable_list.append(li2)

    m = TaxableManipulator()
    total = m.tax_calc(taxable_list)

    print(total) # 145.0
    
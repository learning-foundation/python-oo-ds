from taxable import TaxableMixIn

class LifeInsurance(TaxableMixIn):

    def __init__(self, value, owner, number):
        self._value = value
        self._owner = owner
        self._number = number

    def get_tax_value(self):
        return 50 + self._value * 0.05
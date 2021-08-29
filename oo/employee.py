class Employee:

    def __init__(self, name, doc_number, salary):
        self._name = name
        self._doc_number = doc_number
        self._salary = salary

    def get_bonus(self):
        return self._salary * 0.10
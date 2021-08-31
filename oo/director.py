from employee import Employee

class Director(Employee):

    def __init__(self, name, doc_number, salary):
        super().__init__(name, doc_number, salary)

    def get_bonus():
        return 1000.0
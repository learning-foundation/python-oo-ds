from employee import Employee

class Manager(Employee):
    
    def __init__(self, name, doc_number, salary, password, employee_qt):
        super().__init__(name, doc_number, salary)
        self._password = password
        self._employee_qt = employee_qt

    def authentication(self, password):
        if self._password == password:
            print('access granted')
            return True
        else:
            print('access denied')
            return False
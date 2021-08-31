import abc

class Employee(abc.ABC):

    def __init__(self, name, doc_number, salary):
        self._name = name
        self._doc_number = doc_number
        self._salary = salary

    @abc.abstractmethod
    def get_bonus(self):
        pass
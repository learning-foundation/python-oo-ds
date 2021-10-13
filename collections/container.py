from collections.abc import MutableSequence
from employee import Employee

class Employees(MutableSequence):

    _data = []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, pos):
        return self._data[pos]

    def __setitem__(self, pos, value):
        if (isinstance(value, Employee)):
            self._data[pos] = value
        else:
            raise TypeError('Only Employee is accepted as a value')

    def __delitem__(self, pos):
        del self._data[pos]

    def insert(self, pos, value):
        if (isinstance(value, Employee)):
            return self._data.insert(pos, value)
        else:
            raise TypeError('Only Employee is accepted as a value')

if __name__ == '__main__':
    employess = Employees()
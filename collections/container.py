from collections.abc import MutableSequence

class Employees(MutableSequence):

    _data = []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, pos):
        return self._data[pos]

    def __setitem__(self, pos, value):
        self._data[pos] = value

    def __delitem__(self, pos):
        del self._data[pos]

    def insert(self, pos, value):
        return self._data.insert(pos, value)

if __name__ == '__main__':
    employess = Employees()
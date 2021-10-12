from collections import UserDict # emulator of a dict

class Pins(UserDict):

    def __contains__(self, key):
        return str(key) in self.keys()

    def __setitem__(self, key, value):
        self.data[str(key)] = value

if __name__=='__main__':
    print('collections')
    pins = Pins(one=1)
    print(pins)
    pins[3] = 1
    print(pins)
    my_list = [1, 2, 3]
    pins[my_list] = 2
    print(pins)
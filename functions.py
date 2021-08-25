def average_velocity(distance, time):
    if (time <= 0):
        return distance
    velocity = div(distance, time)
    return velocity

def sum(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1 - number_2

def calc(number_1, number_2):
    return number_1 + number_2, number_1 - number_2, number_1 * number_2, number_1 / number_2

def div(number_1, number_2):
    return number_1 / number_2

def test_args_kwargs(arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)

args = ('one', 2, 3)
test_args_kwargs(*args)

kwargs = {'arg3': 3, 'arg2': 'two', 'arg1': 'one'}
test_args_kwargs(**kwargs)
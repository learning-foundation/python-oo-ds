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

print(average_velocity(100, 20))
print(average_velocity(-20, 10))
print(average_velocity(150, 0))
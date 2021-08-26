import random

def start_message():
    print('******************************')
    print('*        Guessing Game       *')
    print('******************************')

def round_message(round_number, total_guess, guess_string):
    print('Trying {} of {}'.format(round_number, total_guess))
    print('Do you type ' + guess_string)

def choose_level():
    level = 0
    while (level < 1 or level > 3):
        level = int(input('Choose a dificult level from 1 to 3: '))
    return level

def play():
    start_message()
    secret_number = random.randrange(1, 101)
    level = choose_level()
    total_guess = 20 - (level * 5)
    points = 900 + (100 * level)

    for round_number in range(1, total_guess + 1):

        guess_string = input('Type a number from 1 to 100\n')
        round_message(round_number, total_guess, guess_string)

        guess = int(guess_string)
        win = guess == secret_number
        major = guess > secret_number
        minor = guess < secret_number

        if (win):
            print('Hit!')
            print('Your pontuation is {}'.format(points))
            break
        elif (major):
            if (round_number != total_guess):
                print('Wrong, try a smaller number')
            else:
                print('Wrong')
            points = points - (guess - secret_number)
        elif (minor):
            if (round_number != total_guess):
                print('Wrong, try a bigger number')
            else:
                print('Wrong')
            points = points - (secret_number - guess)
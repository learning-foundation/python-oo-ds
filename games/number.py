def play():
    print('******************************')
    print('*    Number Guess Game       *')
    print('******************************')

    secret_number = 60
    level = 0

    while (level < 1 or level > 3):
        level = int(input('Choose a dificult level from 1 to 3: '))

    total_guess = 20 - (level * 5)
    points = 900 + (100 * level)

    for round_number in range(1, total_guess + 1):
        print('Trying {} of {}'.format(round_number, total_guess))
        guess_string = input('Type a number from 1 to 100\n')
        print('Do you type ' + guess_string)

        guess = int(guess_string)
        win = guess == secret_number
        major = guess > secret_number
        minor = guess < secret_number

        if (win):
            print('Hit!')
            print('Your pontuation is {}'.format(points))
            break
        elif (major):
            print('Wrong, try a smaller number')
            points = points - (guess - secret_number)
        elif (minor):
            print('Wrong, try a bigger number')
            points = points - (secret_number - guess)
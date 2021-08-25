print('*********************************')
print('***  Welcome to Hangman Game! ***')
print('*********************************')

secret_word = 'apple'
hit = False
hanged = False

while (not hit and not hanged):
    guess = input('Letter? ')

    pos = 0
    for letter in secret_word:
        if (guess.upper() == letter.upper()):
            print('I found the letter {} in position {}'.format(letter, pos + 1))
        pos = pos + 1
        print('Playing...')

print('Game Over')
print('*********************************')
print('***  Welcome to Hangman Game! ***')
print('*********************************')

secret_word = 'apple'
correct_letters = ['_', '_', '_', '_', '_']
hit = False
hanged = False

print(correct_letters)
while (not hit and not hanged):
    guess = input('Letter? ')

    pos = 0
    for letter in secret_word:
        if (guess.upper() == letter.upper()):
            correct_letters[pos] = letter
            print('I found the letter "{}" in position {}'.format(letter, pos + 1))
        pos = pos + 1
        
    print(correct_letters)

print('Game Over')
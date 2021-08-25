print('*********************************')
print('***  Welcome to Hangman Game! ***')
print('*********************************')

secret_word = 'apple'
correct_letters = ['_', '_', '_', '_', '_']
hit = False
hanged = False
errors = 0

print(correct_letters)
while (not hit and not hanged):
    guess = input('Letter? ')

    if (guess in secret_word):
        pos = 0
        for letter in secret_word:
            if (guess.upper() == letter.upper()):
                correct_letters[pos] = letter
                print('I found the letter "{}" in position {}'.format(letter, pos + 1))
            pos = pos + 1
    else:
        errors += 1
        
    hanged = errors == 6
    hit = '_' not in correct_letters
    
    print(correct_letters)

if (hit):
    print('You win!')
else:
    print('You loose!')

print('Game Over')
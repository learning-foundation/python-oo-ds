import random

def print_list(list_to_print):
    word = ''
    for letter in list_to_print:
        word = word + ' ' + letter
    print(word)

def play():

    print('*********************************')
    print('***  Welcome to Hangman Game! ***')
    print('*********************************')

    words = []
    with open('games/words.txt', 'r') as file:
        for row in file:
            words.append(row.strip())

    selected_index = random.randrange(0, len(words))
    secret_word = words[selected_index]

    correct_letters = []
    for word in secret_word:
        correct_letters.append('_')

    hit = False
    hanged = False
    errors = 0

    print_list(correct_letters)
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
            print('Letter {} not found'.format(guess))
            errors += 1
            
        hanged = errors == 6
        hit = '_' not in correct_letters

        print_list(correct_letters)

    if (hit):
        print('You win!')
    else:
        print('You loose!')

    print('Game Over')
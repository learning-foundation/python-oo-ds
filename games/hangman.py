import random

def start_message():
    print('*********************************')
    print('***  Welcome to Hangman Game! ***')
    print('*********************************')

def get_secret_word():
    words = []
    with open('games/words.txt', 'r') as file:
        for row in file:
            words.append(row.strip())

    selected_index = random.randrange(0, len(words))
    secret_word = words[selected_index]
    return secret_word

def get_correct_letter(secret_word):
    return ['_' for word in secret_word]

def print_list(list_to_print):
    word = ''
    for letter in list_to_print:
        word = word + ' ' + letter
    print(word)

def insert_correct_guess(guess, secret_word, correct_letters):
    pos = 0
    for letter in secret_word:
        if (guess.upper() == letter.upper()):
            correct_letters[pos] = letter
            print('I found the letter "{}" in position {}'.format(letter, pos + 1))
        pos = pos + 1

def end_message(hit, secret_word):
    if (hit):
        print('You win!')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print('You loose!')
        print('The word was {}'.format(secret_word))
        print("    _______________         ")
        print("   /               \        ")
        print("  /                 \       ")
        print("//                   \/\    ")
        print("\|   XXXX     XXXX   | /    ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/      ")
        print("   |\     XXX     /|        ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/        ")
        print("     \_         _/          ")
        print("       \_______/            ")
    print('Game Over')

def print_gallows(errors):

    if (errors == 1):
        print(' O ')
        return
    
    if (errors == 2):
        print(' O ')
        print(' | ')
        return

    if (errors == 3):
        print(' O ')
        print(' | ')
        print('/  ')
        return

    if (errors == 4):
        print(' O ')
        print(' | ')
        print('/ \\')
        return

    if (errors == 5):
        print(' O ')
        print('-| ')
        print('/ \\')
        return

    if (errors == 6):
        print(' O ')
        print('-|-')
        print('/ \\')
        return


def play():
    start_message()
    secret_word = get_secret_word()
    correct_letters = get_correct_letter(secret_word)
    print_list(correct_letters)

    hit = False
    hanged = False
    errors = 0

    while (not hit and not hanged):
        guess = input('Letter? ')

        if (guess.upper() in secret_word.upper()):
            insert_correct_guess(guess, secret_word, correct_letters)
        else:
            print('Letter {} not found'.format(guess))
            errors += 1
            print_gallows(errors)
            
        hanged = errors == 6
        hit = '_' not in correct_letters

        print_list(correct_letters)

    end_message(hit, secret_word)

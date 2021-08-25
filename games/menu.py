import hangman
import number

print('*********************************')
print('**********  Game Menu  **********')
print('*********************************')
print("1. Hangman")
print("2. Number")
game = int(input("Choose your game: "))

if game == 1:
    hangman.play()
elif game == 2:
    number.play()
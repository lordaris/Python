import random
import string
from string import ascii_lowercase

print("H A N G M A N")

win = 0
lost = 0


def play():
    guess_word = ['python', 'java', 'swift', 'javascript']
    pick_word = random.choice(guess_word)
    global win
    global lost
#    store_word = "-" * len(pick_word)
    lives = 8
    s = set()
    w = set()
    while lives > 0:
        print()
        for k in pick_word:
            if k in s:
                print(k, end='')
            else:
                print('-', end='')

        check_word = input('\nInput a letter: ')
        if check_word not in pick_word and check_word not in w and check_word in ascii_lowercase:
            print('That letter doesn\'t appear in the word')
            lives -= 1
            w.add(check_word)
        elif len(check_word) != 1:
            print("Please, input a single letter")
        elif check_word in w:
            print('You\'ve already guessed this letter')
        elif check_word in s:
            print('You\'ve already guessed this letter')
        elif len(check_word) > 1:
            print('You should print a single letter')
        elif check_word not in string.ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet")
        else:
            s.add(check_word)
        if set(pick_word) == s:
            print('You guessed the word ' + pick_word + '!\nYou survived!')
            win += 1
            break
    else:
        lost += 1
        print('You lost!')


def results():
    print(f"You won: {win} times")
    print(f"You lost: {lost} times")


def menu():
    while True:
        selection = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if selection == "play":
            play()
        elif selection == "results":
            results()
        elif selection == "exit":
            break


menu()

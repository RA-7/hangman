import random
import os
import sys


words = ['pizza','word','python','test','yellow','down','chair','kitties']

secret_word = random.choice(words)
secret_letters = list(secret_word)
blanks = ('_' * len(secret_word))
guess_count = 10
correct_guesses = []


def print_blanks(guess_count):
    print('You have {} guesses remaining!'.format(guess_count))
    print()
    print(blanks)
    print()

os.system('clear')
print_blanks(guess_count)

while guess_count > 0:
    blanks = list(blanks)
    guess = input('Guess a letter: ').lower()
    while not guess.isalpha() or len(guess) > 1:
        print('Please input a single letter!')
        guess = input('Guess a letter: ')
    os.system('clear')
    while (guess in secret_letters) and (guess not in correct_guesses):
        guess_index = secret_letters.index(guess)
        secret_letters[guess_index] = '-'
        blanks[guess_index] = guess
    correct_guesses += guess
    guess_count -= 1
    blanks = ''.join(blanks)
    print_blanks(guess_count)
    if '_' not in blanks:
        print('You win!')
        sys.exit(0)

print('You lose!')


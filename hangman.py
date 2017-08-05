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
    # make sure the user input is a single letter
    while not guess.isalpha() or len(guess) > 1:
        print('Please input a single letter!')
        guess = input('Guess a letter: ')
    os.system('clear')
    while (guess in secret_letters) and (guess not in correct_guesses):
        # get the index of the guessed letter
        guess_index = secret_letters.index(guess)
        # replace the first instance of the guessed letter in the secret
        # word with a dash, so the second instance etc. can be found
        secret_letters[guess_index] = '-'
        # add the guessed letter to the row of blanks at the same index
        blanks[guess_index] = guess
    correct_guesses += guess
    guess_count -= 1
    blanks = ''.join(blanks)
    print_blanks(guess_count)
    if '_' not in blanks:
        print('You win!')
        sys.exit(0)

print('You lose!')


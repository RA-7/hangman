import os
import random
import sys


class Hangman:
    def __init__(self, guess_count=10):
        self.words = ['pizza', 'word', 'python', 'test', 'yellow', 'down',
                      'chair', 'kitties']
        self.secret_word = random.choice(self.words)
        self.blanks = ('_' * len(self.secret_word))
        self.guess_count = guess_count

    def print_blanks(self):
        print('You have {} guesses remaining!'.format(self.guess_count))
        print()
        print(self.blanks)
        print()

    def play(self):
        os.system('clear')
        self.print_blanks()
        secret_letters = list(self.secret_word)
        correct_guesses = []

        while self.guess_count > 0:
            self.blanks = list(self.blanks)
            guess = input('Guess a letter: ').lower()

            # make sure the user input is a single letter
            while not guess.isalpha() or len(guess) > 1:
                print('Please input a single letter!')
                guess = input('Guess a letter: ')
            os.system('clear')

            while (guess in secret_letters) and (guess not in correct_guesses):
                # get the index of the guessed letter
                guess_index = secret_letters.index(guess)
                # replace the first instance of guessed letter in the secret
                # word with a dash, so the second instance etc. can be found
                secret_letters[guess_index] = '-'
                # add the guessed letter to the row of blanks at the same index
                self.blanks[guess_index] = guess

            correct_guesses += guess
            self.guess_count -= 1
            self.blanks = ''.join(self.blanks)
            self.print_blanks()

            if '_' not in self.blanks:
                print('You win!')
                sys.exit(0)

        print('You lose!')


if __name__ == '__main__':
    game = Hangman()
    game.play()

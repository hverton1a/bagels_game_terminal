import random
import sys
from lib.game import *
from lib.player import *
from lib.secret import *


def play_bagels():
    game = Game()
    secret_number = Secret_Number()
    player = Player()

    print(f'Take a guess of a {game.num_of_digits} digit(s) number.\n')
    print(f"Guess #0")

    while True:

        player.take_a_guess(game.num_of_digits)
        if player.is_quitting():
            game.quit()

        if secret_number.is_hit(player.guess):
            game.win(secret_number.secret)
            break
        else:
            print(f"Guess #{str(player.get_num_attempts())}\n")
            print(secret_number.check_guess(player.guess),'\n')

        if game.run_out_attempts( player.get_num_attempts()):
            print("Sorry you run out of guesses.")
            print("\nGame Over!")
            print(secret_number.show())
            break

    print('-'*12)
    print("\nWant to play again?")
    choice = input('y(es) or n(o)\n')
    if (choice.strip().lower() == 'y'):
        play_bagels()
    print('\nThanks for playing!\n')
    print('-'*12)
    game.quit()


if __name__ == '__main__':
    play_bagels()

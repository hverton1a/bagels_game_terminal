import random
import sys
from lib.game import *
from lib.player import *
from lib.secret import *


def play_bagels():
    game = Game()
    secret_number = Secret_Number()
    player = Player()

    while True:

        player.take_a_guess(game.num_of_digits)

        if player.is_quitting():
            game.quit()

        if secret_number.is_hit(player.guess):
            game.win(secret_number.secret)
            break
        else:
            print(secret_number.check_guess(player.guess))

        if game.run_out_attempts( player.get_num_attempts()):
            print("\nGame Over!")
            print("Sorry you run out of guesses.")
            secret_number.show()
            break

    print("\nWant to play again?")
    choice = input('y or n\n')
    if (choice.strip().lower() == 'y'):
        play_bagels()
    print('\nThanks for playing!\n')
    game.quit()


if __name__ == '__main__':
    play_bagels()

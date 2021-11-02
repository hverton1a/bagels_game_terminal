import random
import sys
from lib.game import *
from lib.player import *
from lib.secret import *


def play_bagels(num_of_digits=3, max_attempts=10):

    game = Game(num_of_digits, max_attempts)
    secret_number = Secret_Number(num_of_digits)
    player = Player(num_of_digits)

    print("*** Welcome to Bagels Game! ***\n\n")
    print('Bagels is a logical guessing game, where you try to hit a secret number.\n',
            'You have a limited ammount of attempts.\n',
            'For each digit that match a digit in the secret number,\n but is not in the',
            'right position you receive "Pico".\n',
            'If happens to be in the right position too you receive "Fermi" instead.\n',
            'If you are complete wrong you receive "Bagels"!\n')
    print(f"Good Luck!\n For tis game you have {max_attempts} attempts\n\n")

    print(f'Take a guess of a {game.num_of_digits} digit(s) number.\n')
    print(f"Guess #0")

    while True:

        player.take_a_guess()
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
    num_of_digits = 3
    max_attempts = 10

    if(len(sys.argv)>1):
        try:
            if sys.argv[1] != None and sys.argv[1].isdigit():
                num_of_digits = int(sys.argv[2])

            if sys.argv[2] != None and sys.argv[2].isdigit():
                max_attempts = int(sys.argv[2])
        except:
            pass


    play_bagels(num_of_digits, max_attempts)

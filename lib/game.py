import sys


class Game:
    MAX_ATTEMPTS = 10
    NUM_OF_DIGITS = 3

    def __init__(self, max_attempts = MAX_ATTEMPTS, num_of_digits=NUM_OF_DIGITS):
        self.max_attempts = max_attempts
        self.num_of_digits = num_of_digits

    def quit(self):
        sys.exit()

    def win(self, secret):
        print(f'Congratulations you have hit the Secret Number {secret}.')

    def run_out_attempts(self, player_attempts):
        return player_attempts >= self.max_attempts

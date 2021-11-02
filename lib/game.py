import sys


class Game:
    MAX_ATTEMPTS = 10
    NUM_OF_DIGITS = 3

    def __init__(self, num_of_digits = NUM_OF_DIGITS,  max_attempts = MAX_ATTEMPTS):
        self.max_attempts = max_attempts
        self.num_of_digits = num_of_digits

    def quit(self):
        sys.exit()

    def win(self, secret):
        string_formated_secret = ''.join(str(num) for num in secret)
        print(f'Congratulations you have hit the Secret Number {string_formated_secret}.')

    def run_out_attempts(self, player_attempts):
        return player_attempts >= self.max_attempts

    def get_max_attempts(self):
        return self.max_attempts

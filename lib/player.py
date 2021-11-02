class Player:
    def __init__(self):
        self.num_of_attempts = 0
        self.quit = False

    def take_a_guess(self, number_of_digits):
        self.num_of_attempts += 1
        self.guess = None

        while not self.guess:
            print(f'Insert a {number_of_digits} digit(s) number guess.\n')
            input_guess = input()
            input_guess = input_guess.strip().lower()

            if input_guess == 'quit':
                self.quit = True
                self.guess = input_guess
                break
            elif len(input_guess) != number_of_digits or not input_guess.isdigit() :
                print(f'Please input a valid only digit guess of {number_of_digits} or "quit" to exit.\n')
                continue
            else:
                self.guess = [ int(digit) for digit in input_guess ]
                break

        return self.guess

    def guess(self):
        return self.guess

    def get_num_attempts(self):
        return self.num_of_attempts

    def is_quitting(self):
        return self.quit

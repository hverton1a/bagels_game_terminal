import random

class Secret_Number:
    def __init__(self, num_of_digits=3):
        self.secret = [random.choice(range(0,9)) for x in range(num_of_digits)]


    def is_hit(self, guess):
        result = False
        if len(guess) == len(self.secret):
            result = True
            for digit in range(len(guess)):
                if guess[digit] != self.secret[digit]:
                    result = False
                    break
        return result


    def check_guess(self, guess):
        result = []

        for digit in range(len(guess)):
            if guess[digit] == self.secret[digit]:
                result.append("Fermi")
            elif guess[digit] in self.secret:
                result.append("Pico")

        if len(result) == 0:
            result.append('Bagels')

        random.shuffle(result)
        return ' '.join(result)


    def show(self):
        secret = "".join(str(n) for n in self.secret)
        print('The secret was :',secret)

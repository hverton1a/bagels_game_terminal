import unittest
from unittest.mock import patch
from lib.secret import *


class Bagles_Secret_Number_Test(unittest.TestCase):

    def test_secret_number_instance(self):
        secret_number = Secret_Number()
        self.assertIsNotNone(secret_number.secret)

    def test_secret_number_length(self):
        num_of_digits = 5
        secret_number = Secret_Number(num_of_digits)
        self.assertEqual(len(secret_number.secret), num_of_digits)

    def test_secret_number_is_hit_method(self):
        num_of_digits = random.choice(range(3,10))
        secret_number = Secret_Number(num_of_digits)
        self.assertTrue(secret_number.is_hit(secret_number.secret))

    def test_secret_number_check_guess_method_pico_pico_response(self):
        num_of_digits = 3
        secret_number = Secret_Number(num_of_digits)
        mock_secret = [1,2,3]
        guess = secret_number.secret.copy()
        random.shuffle(guess)
        for i in range(0,9):
            if i not in secret_number.secret:
                guess[0] = i
                break

        result = secret_number.check_guess(guess)

        self.assertEqual(result, 'Pico Pico')


    def test_secret_number_check_guess_method_bagels_response(self):
                num_of_digits = 3
                secret_number = Secret_Number(num_of_digits)
                guess = secret_number.secret.copy()

                for i in range(0,9):
                    if i not in secret_number.secret:
                        guess[0] = i
                        guess[1] = i
                        guess[2] = i
                        break

                result = secret_number.check_guess(guess)

                self.assertEqual(result, 'Bagels')

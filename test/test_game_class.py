import unittest
from unittest.mock import patch
import random
from lib.game import *


class Bagles_Game_Test(unittest.TestCase):

    def test_default_game_instance(self):
        for i in range(1,4):
            num_of_digits = random.choice(range(3,10))
            max_attempts = random.choice(range(10,20))
            game = Game(max_attempts, num_of_digits)
            self.assertEqual(game.num_of_digits, num_of_digits)
            self.assertEqual(game.max_attempts, max_attempts)


    def test_game_method_quit(self):
        game = Game()
        with self.assertRaises(SystemExit):
            game.quit()


    @patch('builtins.print')
    def test_game_method_win(self, mock_print):
        game = Game()
        secret = 123
        game.win(secret)
        mock_print.assert_called_with(f'Congratulations you have hit the Secret Number {secret}.')


    def test_game_method_run_out_attempts_return_true(self):
        game = Game()
        attempts = 11
        self.assertTrue(game.run_out_attempts(attempts))


    def test_game_method_run_out_attempts_return_false(self):
        game = Game()
        attempts = 4
        self.assertFalse(game.run_out_attempts(attempts))

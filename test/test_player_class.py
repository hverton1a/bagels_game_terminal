import unittest
from unittest.mock import patch
from lib.player import *


class Bagles_Player_Test(unittest.TestCase):

    @patch('builtins.input', lambda *args: '123')
    def test_player_take_a_guess_input_digits_return_list_of_number(self):
        player = Player(3)
        guess = player.take_a_guess()
        self.assertEqual(guess, [1,2,3])

    @patch('builtins.input', lambda *args: '       123     ')
    def test_player_take_a_guess_input_digits_with_left_rigth_whitespaces_return_list_of_number(self):
        player = Player(3)
        guess = player.take_a_guess()
        self.assertEqual(guess, [1,2,3])

    @patch('builtins.input', lambda *args: 'qUiT')
    def test_player_take_a_guess_quit_input_return_string_quit(self):
        player = Player(3)
        guess = player.take_a_guess()
        self.assertEqual(guess, 'quit')

    @patch('builtins.input', lambda *args: '      qUiT       ')
    def test_player_take_a_guess_quit_with_whitespaces_input_return_list_of_number(self):
        player = Player(3)
        guess = player.take_a_guess()
        self.assertEqual(guess, 'quit')

    @patch('builtins.input', lambda *args: '      12345       ')
    def test_player_guess_method_return_the_guess(self):
        player = Player(5)
        guess = player.take_a_guess()
        self.assertEqual(guess, player.guess)

    @patch('builtins.input', lambda *args: '      12345       ')
    def test_player_num_of_guesses_method_return_the_number_of_guesses_taken(self):
        player = Player(5)
        total_guesses = 5
        for i in range(0, total_guesses):
            guess = player.take_a_guess()
        self.assertEqual(total_guesses, player.num_of_attempts)

    @patch('builtins.input', lambda *args: '      12345       ')
    def test_player_is_quitting_method_return_false(self):
        player = Player(5)
        guess = player.take_a_guess()
        self.assertEqual(False, player.is_quitting())

    @patch('builtins.input', lambda *args: '      QUit       ')
    def test_player_is_quitting_method_return_true(self):
        player = Player(5)
        guess = player.take_a_guess()
        self.assertEqual(True, player.is_quitting())

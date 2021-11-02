import unittest
from unittest.mock import patch
from lib.game import *
from bagels import *

class Bagles_Game_Test(unittest.TestCase):

    @patch("lib.player.Player.is_quitting")
    @patch("lib.player.Player.take_a_guess")
    @patch('builtins.input', side_effect=['quit','n'])
    def test_the_Bagels_game_quit(self, mock_player_is_quitting, mock_player_take_a_guess, mock_input):
        with self.assertRaises(SystemExit):
            mock_player_take_a_guess.return_value = 'quit'
            mock_player_is_quitting.return_value = True
            play_bagels()

    @patch("lib.secret.Secret_Number.is_hit")
    @patch("lib.game.Game.run_out_attempts")
    @patch('builtins.input', side_effect=['123','n'])
    def test_the_Bagels_game_run_out_attempts(self, mock_is_hit, mock_run_out, mock_input):
        with self.assertRaises(SystemExit):
            mock_is_hit.return_value = False
            mock_run_out.return_value = True
            play_bagels()

    @patch("lib.player.Player.take_a_guess")
    @patch("lib.secret.Secret_Number.is_hit")
    @patch('builtins.input', lambda *args: 'n')
    def test_the_Bagels_game_player_guess_right(self, mock_take_a_guess, mock_is_hit):
        with self.assertRaises(SystemExit):
            mock_take_a_guess.return_value = [2,3,4]
            mock_is_hit.return_value = True
            play_bagels()

    @patch("lib.player.Player.take_a_guess")
    @patch("lib.secret.Secret_Number.is_hit")
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['n'])
    def test_the_Bagels_game_player_guess_right_test_thanks_output(self, mock_take_a_guess, mock_is_hit, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            mock_take_a_guess.return_value = [2,3,4]
            mock_is_hit.return_value = True
            play_bagels()
            mock_print.assert_called_with("\nWant to play again?")
            mock_print.assert_called_with('Thanks for playing!')

    @patch("lib.player.Player.take_a_guess")
    @patch("lib.secret.Secret_Number.is_hit")
    @patch('builtins.input', side_effect=['y', 'n'])
    def test_the_Bagels_game_player_guess_right_and_replay(self, mock_take_a_guess, mock_is_hit, mock_input):
        with self.assertRaises(SystemExit):
            mock_take_a_guess.return_value = [2,3,4]
            mock_is_hit.return_value = True
            play_bagels()

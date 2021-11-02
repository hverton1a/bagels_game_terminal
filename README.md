#  Bagels Game
#### Terminal version

A simple guessing game.

The player is prompted for a guess number and have a certain amount of tries to
to guess the secret number.

For each right digit in the wrong position the player will receive "Pico" clue.
If this number is also in the right position then "Fermi" will be receives.
And if it all wrong will receive "Bagels".


The game can be started with any amount of digits for the secret number and any
amount of attempts, given as arguments by the console when starting
the script, if any is given, then default will be 3 digits and 10 attempts.

Example: \
`$python3 bagels.py 5 15`\
Will start the game with a secret number of 5 digits with 15 attempts

![GamePlay sample](https://github.com/hverton1a/bagels_game_terminal/blob/main/assets/play.gif)


I´ve started with a AIO function then refactored to classes:
* Game class: containing the win, quit and check if
the player still have attempts.
* Player class: handling the guesses, prompting and storing then, and the quit intention input
* Secret Number class: handling the secret number generation, the compare with and given guess and the clues if not guessed right.

Also use the simplicity of this project to set some automatic tests with unittest and pytest.
![Test report](https://github.com/hverton1a/bagels_game_terminal/blob/main/assets/tests.gif)

[Try it live on Replit!](https://replit.com/@Horvatbarbosa/bagelsgameterminal?v=1)

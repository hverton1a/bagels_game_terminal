#  Rock Paper Scissor
#### Terminal version

A simple game of one player versus random choices.

The player is prompted for 0 as Rock, 1 as Paper or 2 as Scissor the luck against the 'machine'.

If the input is any other the above, will be prompted again for a valid input, the player can input an empty or 'quit' to leave the game.

![GamePlay sample](https://github.com/hverton1a/rockpaperscissor_terminal/blob/main/assets/play.gif)

I use a dictionary to store the 'weakness' of a play, and use a simple if to compare.

* If both play the same is tied.
* If the 'weakness' of the player if equal the adversary play, sorry you loose.
* Finaly if any above you won.

Also use the simplicity of this project to set some automatic tests with unittest and pytest.
![Test report](https://github.com/hverton1a/rockpaperscissor_terminal/blob/main/assets/tests.gif)

[Try it live on Replit!](https://replit.com/@Horvatbarbosa/rockpaperscissorterminal?v=1)

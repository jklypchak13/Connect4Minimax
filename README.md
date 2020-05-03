# Connect 4 Minimax

This project is a sample implementation of the minimax algorithm playing Connect 4. This project is still very much a work in progress, so please do not judge too hard :)

As of right now, the game will play by itself, with both players being controlled by the AI.

## Description

### Minimax

The minimax algorithm is a useful algorithm for finding optimal play in many simple games, like
Tic-Tac-Toe, Connect 4, Chess, and the like. It involves searching through the possible game states and selecting the best one, while assuming optimal play from the opponent.

Here is a description of the [minimax algorithm](https://en.wikipedia.org/wiki/Minimax).

### Alpha-Beta Pruning

In order to increase the efficienc of run time, we utilize alpha beta pruning. A description of alpha beta pruning can be found [here](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

### Depth-Limit

In order to account for the fact that Connect 4 is a complex game with trillions of possible game states, this version was implemented to not search through all possible game states, but instead only look so deep into the search tree. This essentially translates to looking n turns ahead, where n is the depth limit.

### Heuristic

Due to the depth limit, we can not assign a score to the final game state during each iteration. Instead, a heuristic was necessary to essentially estimate how likely a board would result in a win for either side. Right now the heuristic is based on whether a player one, the number of pairs of 2, pairs of 3, and pieces in the center column. This will hopefully be adjusted in the future to be more dynamic.

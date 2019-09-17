# NumPuzzle

Project that implements classes simulating a Number Slider Puzzle, that is also compatible with graph search algorithms.

## Number Slider Puzzle

Number Slider Puzzles are a board of size AxB (usually 3x3) with each tile having a unique number between 1 and A * B - 1 (1 through 8 in a 3x3 board), and the last tile being empty (implemented as a tile with the number zero).

The player starts with a randomly shuffled board such as:

```
╔═╦═╦═╗
║6║4║ ║
╠═╬═╬═╣
║5║1║3║
╠═╬═╬═╣
║8║2║7║
╚═╩═╩═╝
```

And the objective is to get the board to an ordered state such as:


```
╔═╦═╦═╗    ╔═╦═╦═╗
║1║4║7║    ║1║2║3║
╠═╬═╬═╣    ╠═╬═╬═╣
║2║5║8║ or ║4║5║6║
╠═╬═╬═╣    ╠═╬═╬═╣
║3║6║ ║    ║7║8║ ║
╚═╩═╩═╝    ╚═╩═╩═╝
```

Where the only allowed moves are swapping the position of the empty tile with a tile directly neighboring it (not counting diagonals or wraparounds).

e.g.: in the shuffled board the only legal moves are moving 4 to the right or moving 3 up.

## Graph Support

This project also aims to have support for graph search algorithms capable of solving NumPuzzles. Each node is a different NumPuzzle board, with it's neighbors being the boards resulting from the usage of one of their legal moves.

e.g.: given the board:

```
╔═╦═╦═╗
║3║5║6║
╠═╬═╬═╣
║ ║2║1║
╠═╬═╬═╣
║7║4║8║
╚═╩═╩═╝
```

The board itself represents a node, and it's neighbors are the boards which result from doing one of it's legal moves:

Move a tile up (in this case 7):

```
╔═╦═╦═╗
║3║5║6║
╠═╬═╬═╣
║7║2║1║
╠═╬═╬═╣
║ ║4║8║
╚═╩═╩═╝
```

Move a tile down (in this case 3):

```
╔═╦═╦═╗
║ ║5║6║
╠═╬═╬═╣
║3║2║1║
╠═╬═╬═╣
║7║4║8║
╚═╩═╩═╝
```

Move a tile left (in this case 2):

```
╔═╦═╦═╗
║3║5║6║
╠═╬═╬═╣
║2║ ║1║
╠═╬═╬═╣
║7║4║8║
╚═╩═╩═╝
```

Note that the maximum number of legal moves (and consequently node neighbors) is four: up, down, left and right. And also that this board doesn't have a legal "right" move.

The graph generated from this definition has no weights on vertices or edges. And is by definition a undirected graph since if the edge A->B exists, then the edge B->A also exists.

Note that a AxB sized board has (A * B)! different combinations (9! = 362880 for a 3x3 sized board). And since the project aims to support boards of any size (barring memory limits and overflow errors), the graphs themselves will not be instantiated. Rather, each node will be iterated over, and a hash will be used when necessary to differentiate between nodes.

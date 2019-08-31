import math
from random import randrange
from typing import List


class NumPuzzle:
    def __init__(self, size_x: int = 3, size_y: int = 3, board: List[int] = None, seed: int = None, random: bool = True) -> None:
        self._size_x = size_x
        self._size_y = size_y

        if board is not None:
            self.board = board
        elif seed is not None:
            self.seed = seed
        elif random is True:
            self.seed = randrange(size_x * size_y)
        else:
            raise ValueError

    @property
    def size_x(self) -> int:
        return self._size_x

    @property
    def size_y(self) -> int:
        return self._size_y

    @property
    def seed(self) -> int:
        elements = [i for i in range(1, self.size_x * self.size_y)] + [0]
        board = self.board
        seed = 0

        for index in range(0, len(board)):
            seed += elements.index(board[index]) * math.factorial(len(board) - index - 1)

        return seed

    @seed.setter
    def seed(self, value: int) -> None:
        if not 0 <= value < self.size_x * self.size_y:
            raise ValueError

        elements = [i for i in range(1, self.size_x * self.size_y)] + [0]
        board = []

        for i in range(self.size_x * self.size_y, 0, -1):
            index = value // math.factorial(i - 1)
            value %= math.factorial(i - 1)
            board.append(elements.pop(index))

        self.board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value) -> None:
        if len(value) != self.size_x * self.size_y:
            raise ValueError

        for element in range(0, self.size_x * self.size_y):
            if element not in value:
                raise ValueError

        self._board = dict()

    def neighbors(self):
        pass

    def is_solved(self) -> bool:
        return self.seed == 0

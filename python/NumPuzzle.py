import math
from random import randrange


class NumPuzzle:
    def __init__(self, size_x: int = 3, size_y: int = 3, seed: int = None, board = None, random: bool = True) -> None:
        self.size_x = size_x
        self.size_y = size_y

        if board is not None:
            if len(board) != size_x * size_y:
                raise ValueError

        elif seed is not None and 0 <= seed < math.factorial(size_x * size_y):
            self.seed = seed
        elif random is True:
            self.seed = randrange(size_x * size_y)
        else:
            raise ValueError

    @property
    def size_x(self) -> int:
        return self._size_x

    @size_x.setter
    def size_x(self, value: int) -> None:
        self._size_x = value

    @property
    def size_y(self) -> int:
        return self._size_y

    @size_y.setter
    def size_y(self, value: int) -> None:
        self._size_y = value

    @property
    def seed(self) -> int:
        return self._seed

    @seed.setter
    def seed(self, value: int) -> None:
        self._seed = value

    @property
    def board(self):
        elements = [i for i in range(1, self.size_x * self.size_y)] + [0]
        sequence = []
        seed = self.seed

        for i in range(self.size_x * self.size_y, 0, -1):
            index = seed // math.factorial(i - 1)
            seed %= i
            sequence.append(elements.pop(index))

        return sequence

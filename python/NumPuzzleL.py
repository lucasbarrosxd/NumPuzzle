# Bibliotecas importadas.
from bisect import bisect
from math import factorial
from random import randrange
from typing import Optional, Tuple, List


class NumPuzzle:
    def __init__(self,
                 size: Tuple[int, int] = (3, 3),
                 board: Optional[List[List[int]]] = None,
                 seed: Optional[int] = None,
                 random: bool = True) -> None:

        self._size_x = size[0]
        self._size_y = size[1]

        if board is not None:
            self.board = board
        elif seed is not None:
            self.seed = seed
        elif random:
            self.seed = randrange(factorial(size[0] * size[1]))
        else:
            raise ValueError

    @property
    def size_x(self) -> int:
        return self._size_x

    @property
    def size_y(self) -> int:
        return self._size_y

    def _at(self, position: Tuple[int, int]) -> Optional[int]:
        raise NotImplementedError
    __matmul__ = _at

    def _find(self, num: Optional[int]) -> Tuple[int, int]:
        raise NotImplementedError
    __rmatmul__ = _find

    @property
    def seed(self) -> int:
        board_sequence = [number for col in self.board for number in col]
        seed = 0

        # Sequence from where the numbers would be extracted from when calculating board from seed.
        number = board_sequence.pop()
        numbers = [number if number != 0 else self.size_x * self.size_y]
        for index in range(1, self.size_x * self.size_y):
            # Get last number.
            number = board_sequence.pop()
            # Find position where the given number would be placed.
            if number != 0:
                # Find where the number would place.
                position = bisect(numbers, number)
                # Add number to the sequence.
                numbers.insert(position, number)
            else:
                # Bisect compares numbers but zero needs to be the last number in the sequence.
                position = len(numbers)
                # Appending zero to the end would make the sequence unordered. Instead append a number greater than
                # all numbers that need to be in the sequence.
                numbers.append(self.size_x * self.size_y)
            # Calculate seed change.
            seed += position * factorial(index)

        return seed

    @seed.setter
    def seed(self, value: int) -> None:
        # Seed has (x * y)! combinations. Validate seed.
        if not 0 <= value < factorial(self.size_x * self.size_y):
            raise ValueError

        # List to numbers which haven't been found in the seed yet.
        sequence = list(range(1, self.size_x * self.size_y)) + [0]
        # Initialize board.
        board = list()

        # Find number in each position.
        for index_x in range(self.size_x):
            # Add new column.
            board.append(list())
            for index_y in range(self.size_y):
                # Get factorial which will be used in the divisions.
                fact = factorial(len(sequence) - 1)
                # Calculate next number in the sequence.
                board[index_x].append(sequence.pop(value // fact))
                # Remove the already calculated number from the current seed.
                value %= fact

        self.board = board

    @property
    def board(self) -> List[List[int]]:
        return self._board

    @board.setter
    def board(self, value: List[List[int]]) -> None:
        # Check if number of rows is incorrect.
        if len(value) != self.size_x:
            raise ValueError
        # Check if any row has the wrong number of columns.
        for column in value:
            if len(column) != self.size_y:
                raise ValueError
        # Check if one of each element is present on the board.
        if not set(range(0, self.size_x * self.size_y)).issubset(num for col in value for num in col):
            raise ValueError

        self._board = value

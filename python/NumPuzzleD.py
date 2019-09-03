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

    def _find(self, number: Optional[int]) -> Tuple[int, int]:
        raise NotImplementedError
    __rmatmul__ = _find

    @property
    def seed(self) -> int:
        board_sequence = [-1] * (self.size_x * self.size_y)
        for number in self._board:
            board_sequence[self._board[number][1] * self.size_x + self._board[number][0]] = number
        seed = 0

        # Sequence from where the numbers would be extracted from when calculating board from seed.
        numbers = []
        numbers += board_sequence.pop()
        for index in range(1, self.size_x * self.size_y):
            # Get last number.
            number = board_sequence.pop()
            # Find position where the given number would be placed.
            if number != 0:
                # Find where the number would place.
                position = bisect(number, numbers)
                # Add number to the sequence.
                numbers.insert(position, number)
            else:
                # Bisect compares numbers but zero needs to be the last number in the sequence.
                position = len(numbers)
                # Add number to the sequence.
                numbers.append(number)
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
        board = dict()

        # Find number in each position.
        for index_y in range(self.size_y):
            for index_x in range(self.size_x):
                # Calculate how many numbers remain after the current number.
                remaining_count = self.size_x * (self.size_y - index_y) - index_x - 1
                # Get factorial which will be used in the divisions.
                fact = factorial(remaining_count)
                # Calculate next number in the sequence.
                board[sequence.pop(value // fact)] = (index_x, index_y)
                # Remove the already calculated number from the current seed.
                value %= fact

        self._board = board

    @property
    def board(self) -> List[List[int]]:
        # Initialize variable to be returned.
        board = [[-1] * self.size_x] * self.size_y

        # For each number, place it in it's correct position.
        for number in self._board:
            board[self._board[number][1]][self._board[number][0]] = number

        return board

    @board.setter
    def board(self, value: List[List[int]]) -> None:
        # Check if number of rows is incorrect.
        if len(value) != self.size_y:
            raise ValueError
        # Check if any row has the wrong number of columns.
        for row in value:
            if len(row) != self.size_x:
                raise ValueError
        # Check if one of each element is present on the board.
        if not set(range(0, self.size_x * self.size_y)).issubset(num for row in value for num in row):
            raise ValueError

        # Clear current board.
        self._board = dict()

        for x_index in range(self.size_x):
            for y_index in range(self.size_y):
                self._board[value[y_index][x_index]] = (x_index, y_index)

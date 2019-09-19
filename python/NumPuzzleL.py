"""NumPuzzle implementation that uses a list."""

# Imports ------------------------------------------------------------------------------------------------------------ #
# Imported libraries.
from bisect import bisect
from math import factorial
from random import randrange
# # Typing.
from numbers import Integral
from typing import List, Optional, Text, Tuple
# Imported from project.
from .AbstractNumPuzzle import NumPuzzle as NumPuInterface


class NumPuzzle(NumPuInterface):
    # Constructors --------------------------------------------------------------------------------------------------- #
    def __init__(self,
                 size: Tuple[Integral, Integral] = (3, 3),
                 board: Optional[List[List[Integral]]] = None,
                 seed: Optional[Integral] = None,
                 random: bool = True) -> None:

        # Sizes are immutable. Validate and set them directly.
        if not int(size[0]) > 0 or not int(size[1]) > 0:
            raise ValueError
        self._size = size

        # Make the board.
        if board is not None:
            self.board = board
        elif seed is not None:
            self.seed = seed
        elif random:
            self.seed = randrange(factorial(size[0] * size[1]))
        else:
            raise ValueError

    # Size properties ------------------------------------------------------------------------------------------------ #
    @property
    def size(self) -> Tuple[Integral, Integral]:
        return self._size

    @property
    def size_x(self) -> Integral:
        return self._size[0]

    @property
    def size_y(self) -> Integral:
        return self._size[1]

    # Board properties ----------------------------------------------------------------------------------------------- #
    @property
    def board(self) -> List[List[Integral]]:
        return self._board

    @board.setter
    def board(self, value: List[List[Integral]]) -> None:
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

    # Seed properties ------------------------------------------------------------------------------------------------ #
    @property
    def seed(self) -> Integral:
        board = self.board
        board_sequence = [board[col][row] for row in range(int(self.size_y)) for col in range(int(self.size_x))]
        # Start seed at zero and add to it.
        seed = 0

        # Sequence from where the numbers would be extracted from when calculating board from seed.
        number = board_sequence.pop()
        # Pass zero as size_x * size_y for easier compatibility with sorting algorithms.
        numbers = [number if int(number) != 0 else self.size_x * self.size_y]
        for index in range(1, int(self.size_x * self.size_y)):
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
    def seed(self, value: Integral) -> None:
        # Seed has (x * y)! combinations. Validate seed.
        if not 0 <= int(value) < factorial(self.size_x * self.size_y):
            raise ValueError

        # List of numbers which haven't been found in the seed yet.
        sequence = list(range(1, int(self.size_x * self.size_y))) + [0]
        # Initialize board.
        board = [list() for col in range(int(self.size_x))]

        # Find number in each position.
        for index_y in range(int(self.size_y)):
            for index_x in range(int(self.size_x)):
                # Get factorial which will be used in the divisions.
                fact = factorial(len(sequence) - 1)
                # Calculate next number in the sequence.
                board[index_x].append(sequence.pop(value // fact))
                # Remove the already calculated number from the current seed.
                value %= fact

        self.board = board

    # Other getter-like methods -------------------------------------------------------------------------------------- #
    def _at(self, position: Tuple[Integral, Integral]) -> Integral:
        # Validate indexes.
        if not 0 <= int(position[0]) < int(self.size_x) or not 0 <= int(position[1]) < int(self.size_y):
            raise ValueError

        return self._board[int(position[0])][int(position[1])]

    def _find(self, number: Integral) -> Tuple[Integral, Integral]:
        # Validate number.
        if not 0 <= int(number) < self.size_x * self.size_y:
            raise ValueError

        # Iterate through numbers until the right one is found.
        for index_x in range(int(self.size_x)):
            for index_y in range(int(self.size_y)):
                if self._board[index_x][index_y] == number:
                    return index_x, index_y

    # Operators and magic methods ------------------------------------------------------------------------------------ #
    __matmul__ = _at

    __mod__ = _find

    def __hash__(self) -> Integral:
        return self.seed

    def __eq__(self, other: "NumPuzzle") -> bool:
        # Compare sizes first.
        if self.size != other.size:
            return False

        # Compare using boards. Get boards for efficiency.
        self_board = self.board
        other_board = other.board

        # For each position of the board, compare if they have the same number.
        for index_x in range(int(self.size_x)):
            for index_y in range(int(self.size_y)):
                if self_board[index_x][index_y] != other_board[index_x][index_y]:
                    return False

        return True

    def __str__(self) -> Text:
        # Instantiate a copy of the board for quicker access.
        board = self.board
        # String to be returned.
        string = ""
        # Get number of digits necessary per number.
        digits = len(str(self.size_x * self.size_y - 1))
        # Top boundary.
        string += "╔" + "═" * digits + ("╦" + "═" * digits) * (self.size_x - 1) + "╗" + "\n"
        # Middle section.
        string += "║"
        for x_index in range(int(self.size_x)):
            string += "{1:{0}}║".format(digits, board[x_index][0] if board[x_index][0] != 0 else " ")
        string += "\n"
        for y_index in range(1, int(self.size_y)):
            string += "╠" + "═" * digits + ("╬" + "═" * digits) * (self.size_x - 1) + "╣" + "\n"
            string += "║"
            for x_index in range(int(self.size_x)):
                string += "{1:{0}}║".format(digits, board[x_index][y_index] if board[x_index][y_index] != 0 else " ")
            string += "\n"
        # Bottom boundary.
        string += "╚" + "═" * digits + ("╩" + "═" * digits) * (self.size_x - 1) + "╝"

        return string

    # Instance methods ----------------------------------------------------------------------------------------------- #
    def move(self, direction: Text, on_blank: bool = False) -> None:
        zero_x, zero_y = self._find(0)

        if direction == 'L' or direction == 'R':
            # Horizontal move.
            other_x = int(zero_x) + (1 if on_blank == (direction == 'R') else -1)
            if 0 <= other_x < int(self.size_x):
                # Move is valid.
                board = self.board
                # Swap values.
                board[int(zero_x)][int(zero_y)] = board[other_x][int(zero_y)]
                board[other_x][int(zero_y)] = 0
                self.board = board
            else:
                # Move is invalid. Crossing over a border.
                raise ValueError
        elif direction == 'U' or direction == 'D':
            # Vertical move.
            other_y = int(zero_y) + (1 if on_blank == (direction == 'D') else -1)
            if 0 <= other_y < int(self.size_y):
                # Move is valid.
                board = self.board
                # Swap values.
                board[int(zero_x)][int(zero_y)] = board[int(zero_x)][other_y]
                board[int(zero_x)][other_y] = 0
                self.board = board
            else:
                # Move is invalid. Crossing over a border.
                raise ValueError
        else:
            # Invalid direction.
            raise ValueError

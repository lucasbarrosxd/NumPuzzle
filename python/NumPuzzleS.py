# Imported libraries.
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

        if size[0] <= 0 or size[1] <= 0:
            raise ValueError
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
        # Validate indexes.
        if not 0 <= position[0] < self.size_x or not 0 <= position[1] < self.size_y:
            raise ValueError

        return self.board[position[0]][position[1]]
    __matmul__ = _at

    def _find(self, number: int) -> Tuple[int, int]:
        # Validate number.
        if not 0 <= number < self.size_x * self.size_y:
            raise ValueError

        board = self.board
        # Iterate through numbers until the right one is found.
        for index_x in range(self.size_x):
            for index_y in range(self.size_y):
                if board[index_x][index_y] == number:
                    return index_x, index_y
    __mod__ = _find

    def move(self, direction: str, to_blank: bool = True) -> None:
        pos = self._find(0)

        if direction == 'L' or direction == 'R':
            # Horizontal move.
            other_x = pos[0] + (1 if to_blank != (direction == 'R') else -1)
            if 0 <= other_x < self.size_x:
                # Move is valid.
                board = self.board
                # Swap values.
                board[pos[0]][pos[1]] = board[other_x][pos[1]]
                board[other_x][pos[1]] = 0
                self.board = board
            else:
                # Move is invalid. Crossing over a border.
                raise ValueError
        elif direction == 'U' or direction == 'D':
            # Vertical move.
            other_y = pos[1] + (1 if to_blank != (direction == 'D') else -1)
            if 0 <= other_y < self.size_y:
                # Move is valid.
                board = self.board
                # Swap values.
                board[pos[0]][pos[1]] = board[pos[0]][other_y]
                board[pos[0]][other_y] = 0
                self.board = board
            else:
                # Move is invalid. Crossing over a border.
                raise ValueError
        else:
            # Invalid move argument.
            raise ValueError

    @property
    def seed(self) -> int:
        return self._seed

    @seed.setter
    def seed(self, value: int) -> None:
        # Seed has (x * y)! combinations. Validate seed.
        if not 0 <= value < factorial(self.size_x * self.size_y):
            raise ValueError

        self._seed = value

    @property
    def board(self) -> List[List[int]]:
        # Seed value needs to be changed when calculating.
        seed = self.seed
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
                board[index_x].append(sequence.pop(seed // fact))
                # Remove the already calculated number from the current seed.
                seed %= fact

        return board

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

        board_sequence = [number for row in value for number in row]
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

        self.seed = seed

    def __str__(self) -> str:
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
        for x_index in range(self.size_x):
            string += "{1:{0}}║".format(digits, board[x_index][0] if board[x_index][0] != 0 else " ")
        string += "\n"
        for y_index in range(1, self.size_y):
            string += "╠" + "═" * digits + ("╬" + "═" * digits) * (self.size_x - 1) + "╣" + "\n"
            string += "║"
            for x_index in range(self.size_x):
                string += "{1:{0}}║".format(digits, board[x_index][y_index] if board[x_index][y_index] != 0 else " ")
            string += "\n"
        # Bottom boundary.
        string += "╚" + "═" * digits + ("╩" + "═" * digits) * (self.size_x - 1) + "╝"

        return string

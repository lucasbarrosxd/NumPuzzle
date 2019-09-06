# Imported from project.
from .AbstractNumPuzzle import AbsNumPuzzle
# Imported libraries.
from bisect import bisect
from copy import deepcopy
from math import factorial
from random import randrange
from typing import Optional, Tuple, List, Dict


class NumPuzzle(AbsNumPuzzle):
    def __init__(self,
                 size: Tuple[int, int] = (3, 3),
                 board: Optional[List[List[int]]] = None,
                 seed: Optional[int] = None,
                 random: bool = True) -> None:

        super().__init__(size)
        if board is not None:
            self.board = board
        elif seed is not None:
            self.seed = seed
        elif random:
            self.seed = randrange(factorial(size[0] * size[1]))
        else:
            raise ValueError

    def __hash__(self) -> int:
        return self.seed

    def __eq__(self, other: "NumPuzzle") -> bool:
        if self.size != other.size:
            return False

        self_board = self.board
        other_board = other.board

        for index_x in range(len(self_board)):
            for index_y in range(len(other_board)):
                if self_board[index_x][index_y] != other_board[index_x][index_y]:
                    return False

        return True

    def _at(self, position: Tuple[int, int]) -> int:
        # Validate indexes.
        if not 0 <= position[0] < self.size_x or not 0 <= position[1] < self.size_y:
            raise ValueError

        return self._board[position[0]][position[1]]
    __matmul__ = _at

    def _find(self, number: int) -> Tuple[int, int]:
        # Validate number.
        if not 0 <= number < self.size_x * self.size_y:
            raise ValueError

        # Iterate through numbers until the right one is found.
        for index_x in range(self.size_x):
            for index_y in range(self.size_y):
                if self._board[index_x][index_y] == number:
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

    def neighbors(self) -> Dict[str, "AbsNumPuzzle"]:
        neighbors = dict()

        pos = self._find(0)
        if 0 < pos[0] < self.size_x - 1:
            # Can go both left and right.
            neighbors['L'] = deepcopy(self)
            neighbors['L'].move('L', to_blank=False)
            neighbors['R'] = deepcopy(self)
            neighbors['R'].move('R', to_blank=False)
        elif 0 < pos[0]:
            # Can only go left.
            neighbors['L'] = deepcopy(self)
            neighbors['L'].move('L', to_blank=False)
        elif pos[0] < self.size_x - 1:
            # Can only go right.
            neighbors['R'] = deepcopy(self)
            neighbors['R'].move('R', to_blank=False)
        else:
            # Can't move horizontally.
            pass

        if 0 < pos[1] < self.size_y - 1:
            # Can go both up and down.
            neighbors['U'] = deepcopy(self)
            neighbors['U'].move('U', to_blank=False)
            neighbors['D'] = deepcopy(self)
            neighbors['D'].move('D', to_blank=False)
        elif 0 < pos[1]:
            # Can only go up.
            neighbors['U'] = deepcopy(self)
            neighbors['U'].move('U', to_blank=False)
        elif pos[1] < self.size_y - 1:
            # Can only go down.
            neighbors['D'] = deepcopy(self)
            neighbors['D'].move('D', to_blank=False)
        else:
            # Can't move vertically.
            pass

        return neighbors

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

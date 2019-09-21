"""NumPuzzle interface definition."""

# Imports ------------------------------------------------------------------------------------------------------------ #
# Imported libraries.
from copy import deepcopy
# # Typing
from numbers import Integral
from typing import Callable, Dict, List, Optional, Text, Tuple


class NumPuzzle:
    """Interface for NumPuzzle classes.

    A NumPuzzle is a game which can be represented by a board of tiles, each tile having a unique increasing number
    starting from 1, and a tile that is blank.

    Variables are implementation defined.

    This interface defines base implementations for graph methods and related.
    """
    # Constructors --------------------------------------------------------------------------------------------------- #
    def __init__(self,
                 size: Tuple[Integral, Integral] = (3, 3),
                 board: Optional[List[List[Integral]]] = None,
                 seed: Optional[Integral] = None,
                 random: bool = True,
                 solvable: Optional[bool] = None) -> None:
        """Initialize the NumPuzzle object.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to be initialized.
        size : Tuple[Integral, Integral]
            The dimensions of the NumPuzzle's board. Cannot be changed.
        board : Optional[List[List[Integral]]]
            The matrix representing the board to initialize the NumPuzzle with. If None, the NumPuzzle will try to
            initialize it's board with the seed and/or random parameters.
        seed : Optional[Integral]
            The seed corresponding to a given NumPuzzle's board state. Only applied if the board parameter is None. If
            None, the NumPuzzle will try to initialize it's board with the random parameter.
        random : bool
            Initialize the board with a random seed. Only applied if the board and seed parameters are both None. If
            False, initialization will fail.
        solvable : Optional[bool]
            If True, only construct the object if it's a solvable NumPuzzle. If False, only construct the object if
            it's a non-solvable NumPuzzle. If None, then accept both solvable and non-solvable NumPuzzles.

        Raises
        ------
        ValueError
            If the size parameter has non-positive values.

            If the board parameter's dimensions don't match the size parameter.

            If the matrix in the board parameter has invalid values (values outside the valid range or repeated values).

            If the seed parameter is an invalid value (value outside the valid range).

            If the solvable parameter is True, but a non-solvable board or seed was passed.

            If the solvable parameter is False, but a solvable board or seed was passed.

            If board is None, seed is None and random is False, thus the board didn't initialize.
        """
        raise NotImplementedError
    # Size properties ------------------------------------------------------------------------------------------------ #
    @property
    def size(self) -> Tuple[Integral, Integral]:
        """Get the width and height of the NumPuzzle's board.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to get the sizes of.

        Returns
        -------
        Tuple[Integral, Integral]
            An ordered tuple with two integral values. The first is the width of the NumPuzzle's board, and the second
            is the height of the NumPuzzle's board.
        """
        raise NotImplementedError

    @property
    def size_x(self) -> Integral:
        """Get the width of the NumPuzzle's board.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to get the width of.

        Returns
        -------
        Integral
            The width of the NumPuzzle's board.
        """
        raise NotImplementedError

    @property
    def size_y(self) -> Integral:
        """Get the height of the NumPuzzle's board.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to get the height of.

        Returns
        -------
        Integral
            The height of the NumPuzzle's board.
        """
        raise NotImplementedError

    # Board properties ----------------------------------------------------------------------------------------------- #
    @property
    def board(self) -> List[List[Integral]]:
        """Get the current NumPuzzle's board.

        The board is a matrix representation of the current state of the NumPuzzle. Each XY coordinate of the matrix
        having a different number corresponding to a tile.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle whose board state will be calculated.

        Returns
        -------
        List[List[Integral]]
            A matrix representing the current board state.
        """
        raise NotImplementedError

    @board.setter
    def board(self, value: List[List[Integral]]) -> None:
        """Set the NumPuzzle to the given matrix.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle whose board is to be set.
        value : List[List[Integral]]
            A matrix containing the board to be set to.

        Raises
        ------
        ValueError
            If the 'value' matrix contains a value smaller than zero or greater than 'self''s horizontal size times
            'self''s vertical size.

            If the 'value' matrix contains a value that appears more than once.
        """
        raise NotImplementedError

    # Seed properties ------------------------------------------------------------------------------------------------ #
    @property
    def seed(self) -> Integral:
        """Gets the seed for the current board state.

        The seed is an integer unique to the NumPuzzle's board. Since a board can have (size_x * size_y)! different
        combinations, the seed must be a value between 0 (inclusive) and (size_x * size_y)! (non-inclusive).

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle whose board will have the seed calculated for.

        Returns
        -------
        Integral
            An unique integer representing the board state.
        """
        raise NotImplementedError

    @seed.setter
    def seed(self, value: Integral) -> None:
        """Set the current board state to the given seed.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle whose board state is to be changed.
        value : Integral
            The seed value used to calculate the new board state.

        Raises
        ------
        ValueError
            If the value parameter is outside the valid range. That is, if it's less than 0 or greater than the
            factorial of the product of it's horizontal and vertical sizes.
        """
        raise NotImplementedError

    # Other getter-like methods -------------------------------------------------------------------------------------- #
    def _at(self, position: Tuple[Integral, Integral]) -> Integral:
        """Find which number is at the given position of the NumPuzzle's board.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle whose position will be searched.
        position : Tuple[Integral, Integral]
            The position to be searched in the NumPuzzle's board. Indexing starts from the top-left of the board.

        Returns
        -------
        Integral
            The number of the tile found at the given position of the given board.

        Raises
        ------
        ValueError
            If the given position is invalid. That is, when position[0] is not a number between 0 (inclusive), and the
            NumPuzzle's width (non-inclusive), or when position[1] is not a number between 0 (inclusive) and the
            NumPuzzle's height (non-inclusive).
        """
        raise NotImplementedError

    def _find(self, number: Integral) -> Tuple[Integral, Integral]:
        """Finds the position of a given number on the given NumPuzzle's board.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle whose number will be located.
        number : Integral
            The number whose position is to be located.

        Returns
        -------
        Tuple[Integral, Integral]
            The position of the number found on the NumPuzzle. Given as two XY coordinates. Indexing starts from the
            top-left of the NumPuzzle's board.

        Raises
        ------
        ValueError
            If the number cannot be found in the given NumPuzzle.
        """
        raise NotImplementedError

    # Operators and magic methods ------------------------------------------------------------------------------------ #
    __matmul__ = _at

    __mod__ = _find

    def __hash__(self) -> Integral:
        """Hashes the NumPuzzle to a unique integer.

        Hashes are only unique between NumPuzzles with same sizes.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to be hashed.

        Returns
        -------
        Integral
            The hash value of the NumPuzzle.
        """
        raise NotImplementedError

    def __eq__(self, other: "NumPuzzle") -> bool:
        """Compare two NumPuzzles.

        Parameters
        ----------
        self : NumPuzzle
            The first NumPuzzle to be compared.
        other : NumPuzzle
            The second NumPuzzle to be compared.

        Returns
        -------
        bool
            True if self and board have the same size, and if for each position of each board, self and other have the
            same number at the same position. False otherwise.
        """
        raise NotImplementedError

    def __str__(self) -> Text:
        """Convert NumPuzzle to text format.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to convert to textual format.

        Returns
        -------
        Text
            A multi-line string with a graphical representation of the NumPuzzle's board.
        """
        raise NotImplementedError

    # Instance methods ----------------------------------------------------------------------------------------------- #
    def move(self, direction: Text, on_blank: bool = False) -> None:
        """Execute a move on the given NumPuzzle to change it's state.

        Parameters
        ----------
        self : NumPuzzle
            The board which the move will be applied to.
        direction : Text
            The direction of the move. Must be one of "U", "D", "L" or "R" (representing Up, Down, Left and Right,
            respectively).
        on_blank : bool
            If the move should be applied on the blank tile or on a normal tile. If True, the move will be applied on
            the blank tile, which will move according to the direction parameter. If False, the move will be applied on
            a normal tile, which will move according to the direction parameter.

        Raises
        ------
        ValueError
            If the direction parameter is not one of "U", "D", "L" or "R".

            If the move cannot be completed due to the tile being on one of the edges of the board, and the direction
            being towards that edge of the board.
        """
        raise NotImplementedError

    def polarity(self) -> Integral:
        """Calculate a NumPuzzle's polarity.

        The polarity is the number of inversions in a NumPuzzle board. An inversion occurs when a tile is placed ahead
        of a tile with a greater number, of behind a tile with a smaller number. The blank tile is ignored for these
        calculations.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to calculate polarity for.

        Returns
        -------
        Integral
            The calculated polarity for the NumPuzzle. That is, the number of inversions.
        """

    def is_solvable(self) -> bool:
        """Calculate whether a NumPuzzle can be solved or not.

        Calculation is done using polarity. If the NumPuzzle's polarity is even, it's solvable. If it's odd, it's
        not solvable.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to check if is solvable.

        Returns
        -------
        bool
            True if the NumPuzzle can be solved, False otherwise.
        """
        raise NotImplementedError

    # Graph methods -------------------------------------------------------------------------------------------------- #
    def neighbors(self) -> Dict[Text, "NumPuzzle"]:
        """Calculate boards which can be reached with 1 move.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to calculate the neighbors for.

        Returns
        -------
        Dict[Text, NumPuzzle]
            A dictionary representing the valid moves that can be applied to self. It has at most 4 keys, each being
            one of "U", "L", "D" and "R", representing the directions up, left, down and right, respectively. The value
            associated with each key is the NumPuzzle that results from applying the move that is the key associated
            with the given value.
        """
        # Variable to be returned.
        neighbors = dict()
        # Find the position of the blank tile.
        pos_x, pos_y = self._find(0)
        # Check if the blank tile is near the horizontal edges.
        if 0 < int(pos_x) < int(self.size_x) - 1:
            # Not near any horizontal edges. Can go both left and right.
            neighbors['L'] = deepcopy(self)
            neighbors['L'].move('L', on_blank=True)
            neighbors['R'] = deepcopy(self)
            neighbors['R'].move('R', on_blank=True)
        elif 0 < int(pos_x):
            # Near the right horizontal edge. Can only go left.
            neighbors['L'] = deepcopy(self)
            neighbors['L'].move('L', on_blank=True)
        elif pos_x < self.size_x - 1:
            # Near the left horizontal edge. Can only go right.
            neighbors['R'] = deepcopy(self)
            neighbors['R'].move('R', on_blank=True)
        else:
            # Near both horizontal edges. Can't move horizontally.
            pass

        # Check if the blank tile is near the vertical edges.
        if 0 < int(pos_y) < int(self.size_y) - 1:
            # Not near any vertical edges. Can go both up and down.
            neighbors['U'] = deepcopy(self)
            neighbors['U'].move('U', on_blank=True)
            neighbors['D'] = deepcopy(self)
            neighbors['D'].move('D', on_blank=True)
        elif 0 < int(pos_y):
            # Near the bottom vertical edge. Can only go up.
            neighbors['U'] = deepcopy(self)
            neighbors['U'].move('U', on_blank=True)
        elif pos_y < self.size_y - 1:
            # Near the top vertical edge. Can only go down.
            neighbors['D'] = deepcopy(self)
            neighbors['D'].move('D', on_blank=True)
        else:
            # Near both vertical edges. Can't move vertically.
            pass

        return neighbors

    def breadth_first_search(self) -> Optional[List[Text]]:
        """Calculate a move sequence that solves the given board.

        The move sequence is calculated with the breadth-first search algorithm.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to calculate the move sequence for.

        Returns
        -------
        List[Text]
            An ordered list (starting from zero) of text, each text being one of "D", "L", "U" and "R", each
            representing a valid move (down, left, up, right respectively). If this sequence of moves is applied to
            self, self should become the solved board.
        None
            If there is no path that reaches the solution for the given NumPuzzle.
        """
        # Check beforehand if the NumPuzzle can be solved.
        if not self.is_solvable():
            return None

        # Keep track of nodes that have been discovered. Also keep their parent and the move that was applied to the
        # parent to get the given node, in order to reconstruct the move path later.
        discovered: Dict["NumPuzzle", Tuple[Optional["NumPuzzle"], Optional[Text]]] \
            = {self: (None, None)}
        # Queue with nodes to search.
        puzzles: List["NumPuzzle"] \
            = [self]

        while True:
            # Check if there are reachable puzzles which haven't been searched.
            if len(puzzles) != 0:
                # Get the first puzzle of the list.
                puzzle = puzzles.pop(0)

                # Check if the current puzzle is the solution.
                if puzzle.seed == 0:
                    # Solution found. Get the path to return. Fill path in reverse and then flip it.
                    move_path = []
                    while True:
                        # Check if this puzzle is the starting puzzle.
                        if discovered[puzzle][0] is not None:
                            # Not the starting puzzle. Get the move applied and then check the parent.
                            move_path.append(discovered[puzzle][1])
                            puzzle = discovered[puzzle][0]
                        else:
                            # Found the starting puzzle. Return move sequence.
                            move_path.reverse()
                            return move_path
                else:
                    # Not the solution. Discover neighbors.
                    for direction, neighbor in puzzle.neighbors().items():
                        if neighbor not in discovered:
                            discovered[neighbor] = puzzle, direction
                            puzzles.append(neighbor)
            else:
                # Iterated through all reachable puzzles and didn't find a path to the solution.
                return None

    def heuristic_search(self, heuristic: Callable[["NumPuzzle"], Integral]) -> Optional[List[Text]]:
        """Calculate a move sequence that solves the given board.

        The move sequence is calculated with the heuristic search algorithm.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to calculate the move sequence for.
        heuristic : callable with self, returns an integer
            The heuristic to compare NumPuzzles with.

        Returns
        -------
        List[Text]
            An ordered list (starting from zero) of text, each text being one of "D", "L", "U" and "R", each
            representing a valid move (down, left, up, right respectively). If this sequence of moves is applied to
            self, self should become the solved board.
        None
            If there is no path that reaches the solution for the given NumPuzzle.
        """
        # Check beforehand if the NumPuzzle can be solved.
        if not self.is_solvable():
            return None

        # Keep track of nodes that have been discovered. Also keep their parent and the move that was applied to the
        # parent to get the given node, in order to reconstruct the move path later.
        discovered: Dict["NumPuzzle", Tuple[Optional["NumPuzzle"], Optional[Text]]] \
            = {self: (None, None)}
        # Dictionary with nodes that haven't been searched yet. Keeps the heuristic calculated as value.
        puzzles: Dict["NumPuzzle", Integral] \
            = {self: heuristic(self)}

        while True:
            # Check if there are reachable puzzles which haven't been searched.
            if len(puzzles) != 0:
                # Get one of the puzzles with smallest heuristic.
                puzzle = min(puzzles, key=puzzles.get)
                del puzzles[puzzle]

                # Check if the current puzzle is the solution.
                if puzzle.seed == 0:
                    # Solution found. Get the path to return. Fill path in reverse and then flip it.
                    move_path = []
                    while True:
                        # Check if this puzzle is the starting puzzle.
                        if discovered[puzzle][0] is not None:
                            # Not the starting puzzle. Get the move applied and then check the parent.
                            move_path.append(discovered[puzzle][1])
                            puzzle = discovered[puzzle][0]
                        else:
                            # Found the starting puzzle. Return move sequence.
                            move_path.reverse()
                            return move_path
                else:
                    # Not the solution. Discover neighbors.
                    for direction, neighbor in puzzle.neighbors().items():
                        if neighbor not in discovered:
                            discovered[neighbor] = puzzle, direction
                            puzzles[neighbor] = heuristic(neighbor)
            else:
                # Iterated through all reachable puzzles and didn't find a path to the solution.
                return None

    def astar_search(self, heuristic: Callable[["NumPuzzle"], Integral]) -> Optional[List[Text]]:
        """Calculate a move sequence that solves the given board.

        The move sequence is calculated with the A* search algorithm.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to calculate the move sequence for.
        heuristic : callable with self, returns an integer
            The heuristic to compare NumPuzzles with.

        Returns
        -------
        List[Text]
            An ordered list (starting from zero) of text, each text being one of "D", "L", "U" and "R", each
            representing a valid move (down, left, up, right respectively). If this sequence of moves is applied to
            self, self should become the solved board.
        None
            If there is no path that reaches the solution for the given NumPuzzle.
        """
        # Check beforehand if the NumPuzzle can be solved.
        if not self.is_solvable():
            return None

        # Keep track of nodes that have been discovered. Also keep their parent and the move that was applied to the
        # parent to get the given node, in order to reconstruct the move path later. Also keep the search tree level to
        # apply the algorithm with, starting from level 1.
        discovered: Dict["NumPuzzle", Tuple[Optional["NumPuzzle"], Optional[Text], Integral]] \
            = {self: (None, None, 1)}
        # Dictionary with nodes that haven't been searched yet. Keeps the heuristic calculated as value.
        puzzles: Dict["NumPuzzle", Integral] \
            = {self: heuristic(self) + 1}

        while True:
            # Check if there are reachable puzzles which haven't been searched.
            if len(puzzles) != 0:
                # Get one of the puzzles with smallest heuristic.
                puzzle = min(puzzles, key=puzzles.get)
                del puzzles[puzzle]

                # Check if the current puzzle is the solution.
                if puzzle.seed == 0:
                    # Solution found. Get the path to return. Fill path in reverse and then flip it.
                    move_path = []
                    while True:
                        # Check if this puzzle is the starting puzzle.
                        if discovered[puzzle][0] is not None:
                            # Not the starting puzzle. Get the move applied and then check the parent.
                            move_path.append(discovered[puzzle][1])
                            puzzle = discovered[puzzle][0]
                        else:
                            # Found the starting puzzle. Return move sequence.
                            move_path.reverse()
                            return move_path
                else:
                    # Not the solution. Discover neighbors.
                    for direction, neighbor in puzzle.neighbors().items():
                        if neighbor not in discovered:
                            discovered[neighbor] = puzzle, direction, discovered[puzzle][2] + 1
                            puzzles[neighbor] = heuristic(puzzle) + discovered[neighbor][2]
            else:
                # Iterated through all reachable puzzles and didn't find a path to the solution.
                return None

    def completeness_heuristic(self) -> Integral:
        """Calculate the number of tiles in the incorrect position of the given board.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to calculate the heuristic for.

        Returns
        -------
        Integral
            The number of tiles in the incorrect position in the board.
        """
        current_board = self.board
        incorrect_count = 0

        for row in range(int(self.size_y)):
            for col in range(int(self.size_x)):
                current_num = current_board[col][row]

                correct_x = (current_num - 1) % self.size_x if current_num != 0 else self.size_x - 1
                correct_y = (current_num - 1) // self.size_x if current_num != 0 else self.size_y - 1

                incorrect_count += 1 if col != correct_x or row != correct_y else 0

        return incorrect_count

    def distance_heuristic(self) -> Integral:
        """Calculate a minimum number of moves necessary to get all tiles in the correct positions.

        The minimum number of moves necessary calculated for a given tile is the sum of it's vertical distance to the
        correct position and it's horizontal distance to the correct position. The value returned is the sum of the
        the minimum number of moves necessary for all tiles. Note that this value is not necessarily the number of
        moves the smallest solution uses, but a number of moves smaller than the number of moves of any solution.

        Parameters
        ----------
        self : NumPuzzle
            The NumPuzzle to calculate the heuristic for.

        Returns
        -------
        Integral
            A number smaller than or equal to the minimum number of moves necessary to solve the board. Calculated as
            per the method's description.
        """
        current_board = self.board
        total_distance = 0

        for row in range(int(self.size_y)):
            for col in range(int(self.size_x)):
                current_num = current_board[col][row]

                correct_x = (current_num - 1) % self.size_x if current_num != 0 else self.size_x - 1
                correct_y = (current_num - 1) // self.size_x if current_num != 0 else self.size_y - 1

                total_distance += abs(col - correct_x) + abs(row - correct_y)

        return total_distance

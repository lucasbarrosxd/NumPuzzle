# Import project files.
from NumPuzzle import NumPuzzle
# Import libraries.
import unittest


class Tests(unittest.TestCase):
    def test_p_board_1(self):
        board = NumPuzzle(size_x=2, size_y=2, seed=12).board

        self.assertListEqual(board, [3, 1, 2, 0])

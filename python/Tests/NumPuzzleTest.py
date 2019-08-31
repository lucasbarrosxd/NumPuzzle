# Import project files.
from python.NumPuzzle import NumPuzzle
# Import libraries.
import unittest


class SeedSetterTests(unittest.TestCase):
    def test_s_seed_1(self):
        board = NumPuzzle(size_x=2, size_y=2, seed=0).board
        self.assertListEqual(board, [1, 2, 3, 0])

    def test_s_seed_2(self):
        board = NumPuzzle(size_x=2, size_y=2, seed=12).board
        self.assertListEqual(board, [3, 1, 2, 0])

    def test_s_seed_3(self):
        board = NumPuzzle(size_x=2, size_y=2, seed=23).board
        self.assertListEqual(board, [0, 3, 2, 1])


class SeedPropertyTests(unittest.TestCase):
    def test_p_seed_1(self):
        seed = NumPuzzle(size_x=2, size_y=2, board=[1, 2, 3, 0]).seed
        self.assertEqual(seed, 0)

    def test_p_seed_2(self):
        seed = NumPuzzle(size_x=2, size_y=2, board=[1, 0, 3, 2]).seed
        self.assertEqual(seed, 11)

    def test_p_seed_3(self):
        seed = NumPuzzle(size_x=2, size_y=2, board=[0, 3, 2, 1]).seed
        self.assertEqual(seed, 23)

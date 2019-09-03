# Import from project.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS
# Import libraries.
import math
import unittest
import random


class NumPuzzleTests(unittest.TestCase):
    # NumPuzzle class used. Change to run a unittest with another class.
    NumPuzzle = NumPuzzleD.NumPuzzle

    def test_seed_basic(self):
        """Test basic operations with seed. Give a random 5x5 seed to NumPuzzle and try to get it back."""
        for i in range(10000):
            random_seed = random.randrange(math.factorial(5 * 5))
            recalculated_seed = self.NumPuzzle(size=(5, 5), seed=random_seed).seed
            self.assertEqual(random_seed, recalculated_seed)

    def test_board_basic(self):
        """Test basic operations with board. Give a random 5x5 board to NumPuzzle and try to get it back."""
        for i in range(10000):
            random_sequence = list(range(5*5))
            random.shuffle(random_sequence)
            random_board = [random_sequence[5 * i:5 * i + 5] for i in range(5)]
            calculated_board = self.NumPuzzle(size=(5, 5), board=random_board).board
            for col_index in range(5):
                self.assertListEqual(calculated_board[col_index], random_board[col_index])

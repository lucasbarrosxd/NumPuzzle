# Import from project.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS
# Import libraries.
import math
import unittest
import random


class NumPuzzleTests(unittest.TestCase):
    # NumPuzzle class used. Change to run a unittest with another class.
    NumPuzzle = NumPuzzleL.NumPuzzle

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

    def test_at(self):
        """Test getting a number at a given position. Give a random 5x5 board to NumPuzzle and match all coordinates
        with the original board."""
        for i in range(10000):
            random_sequence = list(range(5 * 5))
            random.shuffle(random_sequence)
            random_board = [random_sequence[5 * i:5 * i + 5] for i in range(5)]
            numpu = self.NumPuzzle(size=(5, 5), board=random_board)
            for index_x in range(5):
                for index_y in range(5):
                    self.assertEqual(random_board[index_x][index_y], numpu @ (index_x, index_y))

    def test_find(self):
        """Test finding at what position a given number is at. Give a random 5x5 board to NumPuzzle and match all
        numbers with the original board."""
        for i in range(10000):
            random_sequence = list(range(5 * 5))
            random.shuffle(random_sequence)
            random_board = [random_sequence[5 * i:5 * i + 5] for i in range(5)]
            numpu = self.NumPuzzle(size=(5, 5), board=random_board)
            for index_x in range(5):
                for index_y in range(5):
                    self.assertEqual((index_x, index_y), numpu % random_board[index_x][index_y])

    def test_seed_to_board_conversion(self):
        # Check the 1x1 board.
        self.assertListEqual(self.NumPuzzle(size=(1, 1), seed=0).board, [[0]])
        # Check all 2x1 boards.
        self.assertListEqual(self.NumPuzzle(size=(2, 1), seed=0).board, [[1], [0]])
        self.assertListEqual(self.NumPuzzle(size=(2, 1), seed=1).board, [[0], [1]])
        # Check all 1x2 boards.
        self.assertListEqual(self.NumPuzzle(size=(1, 2), seed=0).board, [[1, 0]])
        self.assertListEqual(self.NumPuzzle(size=(1, 2), seed=1).board, [[0, 1]])
        # Check all 3x1 boards.
        self.assertListEqual(self.NumPuzzle(size=(3, 1), seed=0).board, [[1], [2], [0]])
        self.assertListEqual(self.NumPuzzle(size=(3, 1), seed=1).board, [[1], [0], [2]])
        self.assertListEqual(self.NumPuzzle(size=(3, 1), seed=2).board, [[2], [1], [0]])
        self.assertListEqual(self.NumPuzzle(size=(3, 1), seed=3).board, [[2], [0], [1]])
        self.assertListEqual(self.NumPuzzle(size=(3, 1), seed=4).board, [[0], [1], [2]])
        self.assertListEqual(self.NumPuzzle(size=(3, 1), seed=5).board, [[0], [2], [1]])
        # Check all 1x3 boards.
        self.assertListEqual(self.NumPuzzle(size=(1, 3), seed=0).board, [[1, 2, 0]])
        self.assertListEqual(self.NumPuzzle(size=(1, 3), seed=1).board, [[1, 0, 2]])
        self.assertListEqual(self.NumPuzzle(size=(1, 3), seed=2).board, [[2, 1, 0]])
        self.assertListEqual(self.NumPuzzle(size=(1, 3), seed=3).board, [[2, 0, 1]])
        self.assertListEqual(self.NumPuzzle(size=(1, 3), seed=4).board, [[0, 1, 2]])
        self.assertListEqual(self.NumPuzzle(size=(1, 3), seed=5).board, [[0, 2, 1]])
        # Check all 2x2 boards.
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=0).board, [[1, 2], [3, 0]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=1).board, [[1, 2], [0, 3]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=2).board, [[1, 3], [2, 0]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=3).board, [[1, 3], [0, 2]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=4).board, [[1, 0], [2, 3]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=5).board, [[1, 0], [3, 2]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=6).board, [[2, 1], [3, 0]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=7).board, [[2, 1], [0, 3]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=8).board, [[2, 3], [1, 0]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=9).board, [[2, 3], [0, 1]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=10).board, [[2, 0], [1, 3]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=11).board, [[2, 0], [3, 1]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=12).board, [[3, 1], [2, 0]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=13).board, [[3, 1], [0, 2]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=14).board, [[3, 2], [1, 0]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=15).board, [[3, 2], [0, 1]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=16).board, [[3, 0], [1, 2]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=17).board, [[3, 0], [2, 1]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=18).board, [[0, 1], [2, 3]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=19).board, [[0, 1], [3, 2]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=20).board, [[0, 2], [1, 3]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=21).board, [[0, 2], [3, 1]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=22).board, [[0, 3], [1, 2]])
        self.assertListEqual(self.NumPuzzle(size=(2, 2), seed=23).board, [[0, 3], [2, 1]])

    def test_board_to_seed_conversion(self):
        # Check the 1x1 board.
        self.assertEqual(self.NumPuzzle(size=(1, 1), board=[[0]]).seed, 0)
        # Check all 2x1 boards.
        self.assertEqual(self.NumPuzzle(size=(2, 1), board=[[1], [0]]).seed, 0)
        self.assertEqual(self.NumPuzzle(size=(2, 1), board=[[0], [1]]).seed, 1)
        # Check all 1x2 boards.
        self.assertEqual(self.NumPuzzle(size=(1, 2), board=[[1, 0]]).seed, 0)
        self.assertEqual(self.NumPuzzle(size=(1, 2), board=[[0, 1]]).seed, 1)
        # Check all 3x1 boards.
        self.assertEqual(self.NumPuzzle(size=(3, 1), board=[[1], [2], [0]]).seed, 0)
        self.assertEqual(self.NumPuzzle(size=(3, 1), board=[[1], [0], [2]]).seed, 1)
        self.assertEqual(self.NumPuzzle(size=(3, 1), board=[[2], [1], [0]]).seed, 2)
        self.assertEqual(self.NumPuzzle(size=(3, 1), board=[[2], [0], [1]]).seed, 3)
        self.assertEqual(self.NumPuzzle(size=(3, 1), board=[[0], [1], [2]]).seed, 4)
        self.assertEqual(self.NumPuzzle(size=(3, 1), board=[[0], [2], [1]]).seed, 5)
        # Check all 1x3 boards.
        self.assertEqual(self.NumPuzzle(size=(1, 3), board=[[1, 2, 0]]).seed, 0)
        self.assertEqual(self.NumPuzzle(size=(1, 3), board=[[1, 0, 2]]).seed, 1)
        self.assertEqual(self.NumPuzzle(size=(1, 3), board=[[2, 1, 0]]).seed, 2)
        self.assertEqual(self.NumPuzzle(size=(1, 3), board=[[2, 0, 1]]).seed, 3)
        self.assertEqual(self.NumPuzzle(size=(1, 3), board=[[0, 1, 2]]).seed, 4)
        self.assertEqual(self.NumPuzzle(size=(1, 3), board=[[0, 2, 1]]).seed, 5)
        # Check all 2x2 boards.
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[1, 2], [3, 0]]).seed, 0)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[1, 2], [0, 3]]).seed, 1)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]]).seed, 2)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[1, 3], [0, 2]]).seed, 3)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[1, 0], [2, 3]]).seed, 4)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[1, 0], [3, 2]]).seed, 5)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[2, 1], [3, 0]]).seed, 6)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[2, 1], [0, 3]]).seed, 7)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[2, 3], [1, 0]]).seed, 8)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[2, 3], [0, 1]]).seed, 9)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[2, 0], [1, 3]]).seed, 10)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[2, 0], [3, 1]]).seed, 11)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[3, 1], [2, 0]]).seed, 12)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[3, 1], [0, 2]]).seed, 13)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[3, 2], [1, 0]]).seed, 14)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[3, 2], [0, 1]]).seed, 15)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[3, 0], [1, 2]]).seed, 16)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[3, 0], [2, 1]]).seed, 17)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[0, 1], [2, 3]]).seed, 18)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[0, 1], [3, 2]]).seed, 19)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[0, 2], [1, 3]]).seed, 20)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[0, 2], [3, 1]]).seed, 21)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[0, 3], [1, 2]]).seed, 22)
        self.assertEqual(self.NumPuzzle(size=(2, 2), board=[[0, 3], [2, 1]]).seed, 23)

    def test_stringify(self):
        # Test 1x1 board.
        string = ("╔═╗\n"
                  "║ ║\n"
                  "╚═╝")
        self.assertEqual(str(self.NumPuzzle(size=(1, 1), seed=0)), string)
        # Test 2x1 board.
        string = ("╔═╦═╗\n"
                  "║1║ ║\n"
                  "╚═╩═╝")
        self.assertEqual(str(self.NumPuzzle(size=(2, 1), seed=0)), string)
        # Test 1x2 board.
        string = ("╔═╗\n"
                  "║1║\n"
                  "╠═╣\n"
                  "║ ║\n"
                  "╚═╝")
        self.assertEqual(str(self.NumPuzzle(size=(1, 2), seed=0)), string)
        # Test 3x1 board.
        string = ("╔═╦═╦═╗\n"
                  "║1║2║ ║\n"
                  "╚═╩═╩═╝")
        self.assertEqual(str(self.NumPuzzle(size=(3, 1), seed=0)), string)
        # Test 2x2 board.
        string = ("╔═╦═╗\n"
                  "║1║3║\n"
                  "╠═╬═╣\n"
                  "║2║ ║\n"
                  "╚═╩═╝")
        self.assertEqual(str(self.NumPuzzle(size=(2, 2), seed=0)), string)
        # Test 1x3 board.
        string = ("╔═╗\n"
                  "║1║\n"
                  "╠═╣\n"
                  "║2║\n"
                  "╠═╣\n"
                  "║ ║\n"
                  "╚═╝")
        self.assertEqual(str(self.NumPuzzle(size=(1, 3), seed=0)), string)
        # Test 3x3 board.
        string = ("╔═╦═╦═╗\n"
                  "║1║4║7║\n"
                  "╠═╬═╬═╣\n"
                  "║2║5║8║\n"
                  "╠═╬═╬═╣\n"
                  "║3║6║ ║\n"
                  "╚═╩═╩═╝")
        self.assertEqual(str(self.NumPuzzle(size=(3, 3), seed=0)), string)
        # Test reversed 3x3 board.
        string = ("╔═╦═╦═╗\n"
                  "║ ║6║3║\n"
                  "╠═╬═╬═╣\n"
                  "║8║5║2║\n"
                  "╠═╬═╬═╣\n"
                  "║7║4║1║\n"
                  "╚═╩═╩═╝")
        self.assertEqual(str(self.NumPuzzle(size=(3, 3), seed=362879)), string)

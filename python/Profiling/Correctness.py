# Import from project.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS
# Import libraries.
import math
import unittest
import random


class NumPuzzleTests(unittest.TestCase):
    # NumPuzzle class used. Change to run a unittest with another class.
    NumPuzzle = NumPuzzleS.NumPuzzle

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

    def test_move(self):
        """Test moving tiles in the puzzle. Test on a solved 3x3 board."""
        numpu = self.NumPuzzle(size=(3, 3), seed=0)
        self.assertRaises(ValueError, numpu.move, 'D', False)
        self.assertRaises(ValueError, numpu.move, 'R', False)
        numpu.move(direction='U', to_blank=False)
        self.assertEqual(numpu._at((2, 2)), 8)
        self.assertEqual(numpu._at((2, 1)), 0)
        self.assertRaises(ValueError, numpu.move, 'R', False)
        numpu.move(direction='U', to_blank=False)
        self.assertEqual(numpu._at((2, 1)), 7)
        self.assertEqual(numpu._at((2, 0)), 0)
        self.assertRaises(ValueError, numpu.move, 'U', False)
        self.assertRaises(ValueError, numpu.move, 'R', False)
        numpu.move(direction='L', to_blank=False)
        self.assertEqual(numpu._at((2, 0)), 4)
        self.assertEqual(numpu._at((1, 0)), 0)
        self.assertRaises(ValueError, numpu.move, 'U', False)
        numpu.move(direction='L', to_blank=False)
        self.assertEqual(numpu._at((1, 0)), 1)
        self.assertEqual(numpu._at((0, 0)), 0)
        self.assertRaises(ValueError, numpu.move, 'U', False)
        self.assertRaises(ValueError, numpu.move, 'L', False)
        numpu.move(direction='D', to_blank=False)
        self.assertEqual(numpu._at((0, 0)), 2)
        self.assertEqual(numpu._at((0, 1)), 0)
        self.assertRaises(ValueError, numpu.move, 'L', False)
        numpu.move(direction='D', to_blank=False)
        self.assertEqual(numpu._at((0, 1)), 3)
        self.assertEqual(numpu._at((0, 2)), 0)
        self.assertRaises(ValueError, numpu.move, 'L', False)
        self.assertRaises(ValueError, numpu.move, 'D', False)
        numpu.move(direction='R', to_blank=False)
        self.assertEqual(numpu._at((0, 2)), 6)
        self.assertEqual(numpu._at((1, 2)), 0)
        self.assertRaises(ValueError, numpu.move, 'D', False)
        numpu.move(direction='R', to_blank=False)
        self.assertEqual(numpu._at((0, 0)), 2)
        self.assertEqual(numpu._at((1, 0)), 1)
        self.assertEqual(numpu._at((2, 0)), 4)
        self.assertEqual(numpu._at((0, 1)), 3)
        self.assertEqual(numpu._at((1, 1)), 5)
        self.assertEqual(numpu._at((2, 1)), 7)
        self.assertEqual(numpu._at((0, 2)), 6)
        self.assertEqual(numpu._at((1, 2)), 8)
        self.assertEqual(numpu._at((2, 2)), 0)
        self.assertRaises(ValueError, numpu.move, 'U', True)
        self.assertRaises(ValueError, numpu.move, 'L', True)
        numpu.move(direction='R', to_blank=True)
        self.assertEqual(numpu._at((0, 2)), 6)
        self.assertEqual(numpu._at((1, 2)), 0)
        self.assertRaises(ValueError, numpu.move, 'U', True)
        numpu.move(direction='R', to_blank=True)
        self.assertEqual(numpu._at((0, 1)), 3)
        self.assertEqual(numpu._at((0, 2)), 0)
        self.assertRaises(ValueError, numpu.move, 'R', True)
        self.assertRaises(ValueError, numpu.move, 'U', True)
        numpu.move(direction='D', to_blank=True)
        self.assertEqual(numpu._at((0, 0)), 2)
        self.assertEqual(numpu._at((0, 1)), 0)
        self.assertRaises(ValueError, numpu.move, 'R', True)
        numpu.move(direction='D', to_blank=True)
        self.assertEqual(numpu._at((1, 0)), 1)
        self.assertEqual(numpu._at((0, 0)), 0)
        self.assertRaises(ValueError, numpu.move, 'R', True)
        self.assertRaises(ValueError, numpu.move, 'D', True)
        numpu.move(direction='L', to_blank=True)
        self.assertEqual(numpu._at((2, 0)), 4)
        self.assertEqual(numpu._at((1, 0)), 0)
        self.assertRaises(ValueError, numpu.move, 'D', True)
        numpu.move(direction='L', to_blank=True)
        self.assertEqual(numpu._at((2, 1)), 7)
        self.assertEqual(numpu._at((2, 0)), 0)
        self.assertRaises(ValueError, numpu.move, 'D', True)
        self.assertRaises(ValueError, numpu.move, 'L', True)
        numpu.move(direction='U', to_blank=True)
        self.assertEqual(numpu._at((2, 2)), 8)
        self.assertEqual(numpu._at((2, 1)), 0)
        self.assertRaises(ValueError, numpu.move, 'L', True)
        numpu.move(direction='U', to_blank=True)
        self.assertEqual(numpu._at((0, 0)), 1)
        self.assertEqual(numpu._at((1, 0)), 4)
        self.assertEqual(numpu._at((2, 0)), 7)
        self.assertEqual(numpu._at((0, 1)), 2)
        self.assertEqual(numpu._at((1, 1)), 5)
        self.assertEqual(numpu._at((2, 1)), 8)
        self.assertEqual(numpu._at((0, 2)), 3)
        self.assertEqual(numpu._at((1, 2)), 6)
        self.assertEqual(numpu._at((2, 2)), 0)

    def test_seed_to_board_conversion(self):
        """Test if given a seed the right board is generated. Test all boards of order 4 or less."""
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
        """Test if given a board the right seed is generated. Test all boards of order 4 or less."""
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

    def test_neighbors(self):
        numpu = self.NumPuzzle(size=(3, 3), seed=0)
        neighbors = numpu.neighbors()

        self.assertTrue('U' in neighbors)
        self.assertTrue('L' in neighbors)
        self.assertFalse('D' in neighbors)
        self.assertFalse('R' in neighbors)

        self.assertListEqual(neighbors['U'].board, [[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        self.assertListEqual(neighbors['L'].board, [[1, 2, 3], [4, 5, 0], [7, 8, 6]])

        neighbors = neighbors['U'].neighbors()
        self.assertTrue('U' in neighbors)
        self.assertTrue('L' in neighbors)
        self.assertTrue('D' in neighbors)
        self.assertFalse('R' in neighbors)

        self.assertListEqual(neighbors['U'].board, [[1, 2, 3], [4, 5, 6], [0, 7, 8]])
        self.assertListEqual(neighbors['L'].board, [[1, 2, 3], [4, 0, 6], [7, 5, 8]])
        self.assertListEqual(neighbors['D'].board, [[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        neighbors = neighbors['L'].neighbors()
        self.assertTrue('U' in neighbors)
        self.assertTrue('L' in neighbors)
        self.assertTrue('D' in neighbors)
        self.assertTrue('R' in neighbors)

        self.assertListEqual(neighbors['U'].board, [[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        self.assertListEqual(neighbors['L'].board, [[1, 0, 3], [4, 2, 6], [7, 5, 8]])
        self.assertListEqual(neighbors['D'].board, [[1, 2, 3], [4, 6, 0], [7, 5, 8]])
        self.assertListEqual(neighbors['R'].board, [[1, 2, 3], [4, 5, 6], [7, 0, 8]])

        neighbors = neighbors['L'].neighbors()
        self.assertTrue('U' in neighbors)
        self.assertFalse('L' in neighbors)
        self.assertTrue('D' in neighbors)
        self.assertTrue('R' in neighbors)

        self.assertListEqual(neighbors['U'].board, [[0, 1, 3], [4, 2, 6], [7, 5, 8]])
        self.assertListEqual(neighbors['D'].board, [[1, 3, 0], [4, 2, 6], [7, 5, 8]])
        self.assertListEqual(neighbors['R'].board, [[1, 2, 3], [4, 0, 6], [7, 5, 8]])

        neighbors = neighbors['U'].neighbors()
        self.assertFalse('U' in neighbors)
        self.assertFalse('L' in neighbors)
        self.assertTrue('D' in neighbors)
        self.assertTrue('R' in neighbors)

        self.assertListEqual(neighbors['D'].board, [[1, 0, 3], [4, 2, 6], [7, 5, 8]])
        self.assertListEqual(neighbors['R'].board, [[4, 1, 3], [0, 2, 6], [7, 5, 8]])

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

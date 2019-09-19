# Import libraries.
import unittest
# Import from project.
# # Import implementations to test.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS

# NumPuzzle class to run tests with. Change to run tests with a different implementation.
NumPuzzle = NumPuzzleL.NumPuzzle


class SeedTests(unittest.TestCase):
    def test_initialization_validation(self):
        # Check if incorrect seeds raise errors.
        # # Check if negative seeds raise errors.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), seed=-1)
        self.assertRaises(ValueError, NumPuzzle, size=(2, 4), seed=-10)
        self.assertRaises(ValueError, NumPuzzle, size=(4, 2), seed=-12345)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 1), seed=-10000000)
        self.assertRaises(ValueError, NumPuzzle, size=(10, 10), seed=-1)
        # # Check if values above the maximum valid seed raise errors.
        # # # Check normal NumPuzzles.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), seed=362880)
        self.assertRaises(ValueError, NumPuzzle, size=(2, 2), seed=24)
        self.assertRaises(ValueError, NumPuzzle, size=(4, 4), seed=20922789888000)
        # # # Check NumPuzzles with different width and height.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 2), seed=720)
        self.assertRaises(ValueError, NumPuzzle, size=(2, 3), seed=720)
        # # # Check edge cases.
        self.assertRaises(ValueError, NumPuzzle, size=(5, 1), seed=120)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 5), seed=120)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 1), seed=1)
        # Check if correct seeds don't raise errors.
        # # Check normal NumPuzzles.
        # # # 3x3 NumPuzzle.
        NumPuzzle(size=(3, 3), seed=0)
        NumPuzzle(size=(3, 3), seed=123456)
        NumPuzzle(size=(3, 3), seed=362879)
        # # # 2x2 NumPuzzle.
        NumPuzzle(size=(2, 2), seed=0)
        NumPuzzle(size=(2, 2), seed=12)
        NumPuzzle(size=(2, 2), seed=23)
        # # # 4x4 NumPuzzle.
        NumPuzzle(size=(4, 4), seed=0)
        NumPuzzle(size=(4, 4), seed=12345678901234)
        NumPuzzle(size=(4, 4), seed=20922789887999)
        # # Check NumPuzzles with different width and height.
        # # # 3x2 NumPuzzle.
        NumPuzzle(size=(3, 2), seed=0)
        NumPuzzle(size=(3, 2), seed=123)
        NumPuzzle(size=(3, 2), seed=719)
        # # # 2x3 NumPuzzle.
        NumPuzzle(size=(2, 3), seed=0)
        NumPuzzle(size=(2, 3), seed=123)
        NumPuzzle(size=(2, 3), seed=719)
        # # Check edge cases.
        # # # 5x1 NumPuzzle.
        NumPuzzle(size=(5, 1), seed=0)
        NumPuzzle(size=(5, 1), seed=112)
        NumPuzzle(size=(5, 1), seed=119)
        # # # 1x5 NumPuzzle.
        NumPuzzle(size=(1, 5), seed=0)
        NumPuzzle(size=(1, 5), seed=112)
        NumPuzzle(size=(1, 5), seed=119)
        # # # 1x1 NumPuzzle.
        NumPuzzle(size=(1, 1), seed=0)

    def test_access(self):
        # Check if given a seed, the same seed can be retrieved.
        # # Check via initialization.
        # # # Check normal NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 3), seed=0).seed, 0)
        self.assertEqual(NumPuzzle(size=(2, 2), seed=0).seed, 0)
        self.assertEqual(NumPuzzle(size=(4, 4), seed=0).seed, 0)
        # # # Check NumPuzzles with different width and height.
        self.assertEqual(NumPuzzle(size=(3, 2), seed=0).seed, 0)
        self.assertEqual(NumPuzzle(size=(2, 3), seed=0).seed, 0)
        # # # Check edge cases.
        self.assertEqual(NumPuzzle(size=(3, 1), seed=0).seed, 0)
        self.assertEqual(NumPuzzle(size=(1, 3), seed=0).seed, 0)
        self.assertEqual(NumPuzzle(size=(1, 1), seed=0).seed, 0)
        # # Check via setter.
        # # Build NumPuzzle with seed. Set seed to maximum seed and try to get maximum seed.
        # # # Check normal NumPuzzles.
        # # # # 3x3 NumPuzzle.
        numpu = NumPuzzle(size=(3, 3), seed=0)
        numpu.seed = 362879
        self.assertEqual(numpu.seed, 362879)
        # # # # 2x2 NumPuzzle.
        numpu = NumPuzzle(size=(2, 2), seed=0)
        numpu.seed = 23
        self.assertEqual(numpu.seed, 23)
        # # # # 4x4 NumPuzzle.
        numpu = NumPuzzle(size=(4, 4), seed=0)
        numpu.seed = 20922789887999
        self.assertEqual(numpu.seed, 20922789887999)
        # # # Check NumPuzzles with different width and height.
        # # # # 3x2 NumPuzzle.
        numpu = NumPuzzle(size=(3, 2), seed=0)
        numpu.seed = 719
        self.assertEqual(numpu.seed, 719)
        # # # # 2x3 NumPuzzle.
        numpu = NumPuzzle(size=(2, 3), seed=0)
        numpu.seed = 719
        self.assertEqual(numpu.seed, 719)
        # # # Check edge cases.
        # # # # 5x1 NumPuzzle.
        numpu = NumPuzzle(size=(5, 1), seed=0)
        numpu.seed = 119
        self.assertEqual(numpu.seed, 119)
        # # # # 1x5 NumPuzzle.
        numpu = NumPuzzle(size=(1, 5), seed=0)
        numpu.seed = 119
        self.assertEqual(numpu.seed, 119)
        # # # # 1x1 NumPuzzle.
        numpu = NumPuzzle(size=(1, 1), seed=0)
        numpu.seed = 0
        self.assertEqual(numpu.seed, 0)

    def test_board_conversion(self):
        # Check if given a seed, the NumPuzzle gives the right board.
        # # Check normal NumPuzzles.
        # # # 3x3 NumPuzzles.
        self.assertListEqual(NumPuzzle(size=(3, 3), seed=0).board, [[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        self.assertListEqual(NumPuzzle(size=(3, 3), seed=362879).board, [[0, 6, 3], [8, 5, 2], [7, 4, 1]])
        # # # 2x2 NumPuzzles.
        self.assertListEqual(NumPuzzle(size=(2, 2), seed=0).board, [[1, 3], [2, 0]])
        self.assertListEqual(NumPuzzle(size=(2, 2), seed=23).board, [[0, 2], [3, 1]])
        # # # 4x4 NumPuzzles.
        self.assertListEqual(NumPuzzle(size=(4, 4), seed=0).board,
                             [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]])
        self.assertListEqual(NumPuzzle(size=(4, 4), seed=20922789887999).board,
                             [[0, 12, 8, 4], [15, 11, 7, 3], [14, 10, 6, 2], [13, 9, 5, 1]])
        # # Check NumPuzzles with different width and height.
        # # # 3x2 NumPuzzles.
        self.assertListEqual(NumPuzzle(size=(3, 2), seed=0).board, [[1, 4], [2, 5], [3, 0]])
        self.assertListEqual(NumPuzzle(size=(3, 2), seed=719).board, [[0, 3], [5, 2], [4, 1]])
        # # # 2x3 NumPuzzles.
        self.assertListEqual(NumPuzzle(size=(2, 3), seed=0).board, [[1, 3, 5], [2, 4, 0]])
        self.assertListEqual(NumPuzzle(size=(2, 3), seed=719).board, [[0, 4, 2], [5, 3, 1]])
        # # Check edge cases.
        # # # 5x1 NumPuzzles.
        self.assertListEqual(NumPuzzle(size=(5, 1), seed=0).board, [[1], [2], [3], [4], [0]])
        self.assertListEqual(NumPuzzle(size=(5, 1), seed=119).board, [[0], [4], [3], [2], [1]])
        # # # 1x5 NumPuzzles.
        self.assertListEqual(NumPuzzle(size=(1, 5), seed=0).board, [[1, 2, 3, 4, 0]])
        self.assertListEqual(NumPuzzle(size=(1, 5), seed=119).board, [[0, 4, 3, 2, 1]])
        # # # 1x1 NumPuzzles.
        self.assertListEqual(NumPuzzle(size=(1, 1), seed=0).board, [[0]])

    def test_board_access(self):
        # Check if given a seed, NumPuzzle can get the seed back after converting it to a board.
        # Build with a seed, get the board, then build with the board and get the seed.
        # # Check with normal NumPuzzles.
        # # # 3x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 3), board=NumPuzzle(size=(3, 3), seed=0).board).seed, 0)
        self.assertEqual(NumPuzzle(size=(3, 3), board=NumPuzzle(size=(3, 3), seed=123456).board).seed, 123456)
        self.assertEqual(NumPuzzle(size=(3, 3), board=NumPuzzle(size=(3, 3), seed=362879).board).seed, 362879)
        # # # 2x2 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(2, 2), board=NumPuzzle(size=(2, 2), seed=0).board).seed, 0)
        self.assertEqual(NumPuzzle(size=(2, 2), board=NumPuzzle(size=(2, 2), seed=12).board).seed, 12)
        self.assertEqual(NumPuzzle(size=(2, 2), board=NumPuzzle(size=(2, 2), seed=23).board).seed, 23)
        # # # 4x4 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(4, 4), board=NumPuzzle(size=(4, 4), seed=0).board).seed, 0)
        self.assertEqual(
            NumPuzzle(size=(4, 4), board=NumPuzzle(size=(4, 4), seed=12345678901234).board).seed, 12345678901234)
        self.assertEqual(
            NumPuzzle(size=(4, 4), board=NumPuzzle(size=(4, 4), seed=20922789887999).board).seed, 20922789887999)
        # # Check NumPuzzles with different width and height.
        # # # 3x2 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 2), board=NumPuzzle(size=(3, 2), seed=0).board).seed, 0)
        self.assertEqual(NumPuzzle(size=(3, 2), board=NumPuzzle(size=(3, 2), seed=123).board).seed, 123)
        self.assertEqual(NumPuzzle(size=(3, 2), board=NumPuzzle(size=(3, 2), seed=719).board).seed, 719)
        # # # 2x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(2, 3), board=NumPuzzle(size=(2, 3), seed=0).board).seed, 0)
        self.assertEqual(NumPuzzle(size=(2, 3), board=NumPuzzle(size=(2, 3), seed=123).board).seed, 123)
        self.assertEqual(NumPuzzle(size=(2, 3), board=NumPuzzle(size=(2, 3), seed=719).board).seed, 719)
        # # Check edge cases.
        # # # 5x1 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(5, 1), board=NumPuzzle(size=(5, 1), seed=0).board).seed, 0)
        self.assertEqual(NumPuzzle(size=(5, 1), board=NumPuzzle(size=(5, 1), seed=112).board).seed, 112)
        self.assertEqual(NumPuzzle(size=(5, 1), board=NumPuzzle(size=(5, 1), seed=119).board).seed, 119)
        # # # 1x5 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(1, 5), board=NumPuzzle(size=(1, 5), seed=0).board).seed, 0)
        self.assertEqual(NumPuzzle(size=(1, 5), board=NumPuzzle(size=(1, 5), seed=112).board).seed, 112)
        self.assertEqual(NumPuzzle(size=(1, 5), board=NumPuzzle(size=(1, 5), seed=119).board).seed, 119)
        # # # 1x1 NumPuzzle.
        self.assertEqual(NumPuzzle(size=(1, 1), board=NumPuzzle(size=(1, 1), seed=0).board).seed, 0)


if __name__ == "__main__":
    unittest.main()

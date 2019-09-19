# Import libraries.
import unittest
# Import from project.
# # Import implementations to test.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS

# NumPuzzle class to run tests with. Change to run tests with a different implementation.
NumPuzzle = NumPuzzleL.NumPuzzle


class BoardTests(unittest.TestCase):
    def test_instantiation_validation(self):
        # Check if incorrect boards raise errors.
        # # Check if a board with invalid sizes raises errors.
        # # # Check if a board with inferior or equal dimensions raises errors.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 4], [2, 5], [3, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 3, 5], [2, 4, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 3], [2, 0]])
        # # # Check if a board with superior or equal dimensions raises errors.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3),
                          board=[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]])
        # # # Check if one size inferior and the other superior raises errors.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 3, 5, 7], [2, 4, 6, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 5], [2, 6], [3, 7], [4, 0]])
        # # # Check if edge cases raise errors.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[0]])
        self.assertRaises(ValueError, NumPuzzle, size=(1, 1), board=[[1, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(1, 1), board=[[1], [0]])
        # # Check if a board with invalid values raises errors.
        # # # Check with negative values.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 2, 3], [4, 5, 6], [7, 8, -1]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[-1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[-1, -2, -3], [-4, -5, -6], [-7, -8, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
        # # # Check with values greater than the maximum allowed value.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 2, 3], [4, 5, 6], [7, 9, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[9, 10, 11], [12, 13, 14], [15, 16, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[9, 10, 11], [12, 13, 14], [15, 16, 17]])
        # # # Check with both types of invalid values.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 2, 3], [-4, 5, 6], [7, 9, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 2, 3], [-4, 5, 6], [7, 8, 9]])
        # # # Check edge cases.
        self.assertRaises(ValueError, NumPuzzle, size=(1, 1), board=[[1]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 1), board=[[1], [2], [3]])
        self.assertRaises(ValueError, NumPuzzle, size=(1, 3), board=[[1, 2, 3]])
        # # Check if a board with duplicated values raises errors.
        # # # Check if a board with only valid duplicates raises errors.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 1]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 1, 7], [2, 5, 8], [3, 6, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        # # # Check if a board with invalid duplicates raises errors.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[-1, -1, 3], [4, 5, 6], [7, 8, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[-1, -1, 3], [4, 5, 6], [7, 8, 2]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 2, 3], [4, 5, 6], [7, 9, 9]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[1, 2, 3], [4, 5, 6], [9, 9, 0]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[-1, -1, 3], [4, 5, 6], [7, 9, 9]])
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=[[-1, -1, 3], [4, 5, 6], [9, 9, 0]])
        # # Check if a board with valid sizes and values doesn't raise errors.
        # # # Check if a normal board size doesn't raise errors.
        NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]])
        NumPuzzle(size=(4, 4), board=[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]])
        # # # Check if different sizes don't raise errors.
        NumPuzzle(size=(3, 2), board=[[1, 4], [2, 5], [3, 0]])
        NumPuzzle(size=(2, 3), board=[[1, 3, 5], [2, 4, 0]])
        # # # Check if edge cases don't raise errors.
        NumPuzzle(size=(1, 1), board=[[0]])
        NumPuzzle(size=(3, 1), board=[[1], [2], [0]])
        NumPuzzle(size=(1, 3), board=[[1, 2, 0]])

    def test_access(self):
        # Check if given a board, the same board can be retrieved.
        # # Setup boards.
        # # # Normal boards.
        board_33 = [[1, 4, 7], [2, 5, 8], [3, 6, 0]]
        board_22 = [[1, 3], [2, 0]]
        board_44 = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]]
        # # # # Reversed.
        board_33r = [[0, 6, 3], [8, 5, 2], [7, 4, 1]]
        board_22r = [[0, 2], [3, 1]]
        board_44r = [[0, 12, 8, 4], [15, 11, 7, 3], [14, 10, 6, 2], [13, 9, 5, 1]]
        # # # Boards with different width and height.
        board_32 = [[1, 4], [2, 5], [3, 0]]
        board_23 = [[1, 3, 5], [2, 4, 0]]
        board_31 = [[1], [2], [0]]
        board_13 = [[1, 2, 0]]
        board_34 = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 0]]
        board_43 = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 0]]
        # # # # Reversed.
        board_32r = [[0, 3], [5, 2], [4, 1]]
        board_23r = [[0, 4, 2], [5, 3, 1]]
        board_31r = [[0], [2], [1]]
        board_13r = [[0, 2, 1]]
        board_34r = [[0, 9, 6, 3], [11, 8, 5, 2], [10, 7, 4, 1]]
        board_43r = [[0, 8, 4], [11, 7, 3], [10, 6, 2], [9, 5, 1]]
        # # # Edge cases.
        board_11 = [[0]]
        # # Check via initialization.
        # # # Check normal boards.
        self.assertListEqual(NumPuzzle(size=(3, 3), board=board_33).board, board_33)
        self.assertListEqual(NumPuzzle(size=(2, 2), board=board_22).board, board_22)
        self.assertListEqual(NumPuzzle(size=(4, 4), board=board_44).board, board_44)
        # # # Check boards with different width and height.
        self.assertListEqual(NumPuzzle(size=(3, 2), board=board_32).board, board_32)
        self.assertListEqual(NumPuzzle(size=(2, 3), board=board_23).board, board_23)
        self.assertListEqual(NumPuzzle(size=(3, 1), board=board_31).board, board_31)
        self.assertListEqual(NumPuzzle(size=(1, 3), board=board_13).board, board_13)
        self.assertListEqual(NumPuzzle(size=(3, 4), board=board_34).board, board_34)
        self.assertListEqual(NumPuzzle(size=(4, 3), board=board_43).board, board_43)
        # # # Check edge cases.
        self.assertListEqual(NumPuzzle(size=(1, 1), board=board_11).board, board_11)
        # # Check via setter.
        # # Build NumPu with board, set to reversed board and try to get the reversed board.
        # # # Check normal boards.
        numpu = NumPuzzle(size=(3, 3), board=board_33)
        numpu.board = board_33r
        self.assertListEqual(numpu.board, board_33r)
        numpu = NumPuzzle(size=(2, 2), board=board_22)
        numpu.board = board_22r
        self.assertListEqual(numpu.board, board_22r)
        numpu = NumPuzzle(size=(4, 4), board=board_44)
        numpu.board = board_44r
        self.assertListEqual(numpu.board, board_44r)
        # # # Check boards with different width and height.
        numpu = NumPuzzle(size=(3, 2), board=board_32)
        numpu.board = board_32r
        self.assertListEqual(numpu.board, board_32r)
        numpu = NumPuzzle(size=(2, 3), board=board_23)
        numpu.board = board_23r
        self.assertListEqual(numpu.board, board_23r)
        numpu = NumPuzzle(size=(3, 1), board=board_31)
        numpu.board = board_31r
        self.assertListEqual(numpu.board, board_31r)
        numpu = NumPuzzle(size=(1, 3), board=board_13)
        numpu.board = board_13r
        self.assertListEqual(numpu.board, board_13r)
        numpu = NumPuzzle(size=(4, 3), board=board_43)
        numpu.board = board_43r
        self.assertListEqual(numpu.board, board_43r)
        numpu = NumPuzzle(size=(3, 4), board=board_34)
        numpu.board = board_34r
        self.assertListEqual(numpu.board, board_34r)
        # # # Check edge case.
        numpu = NumPuzzle(size=(1, 1), board=board_11)
        numpu.board = board_11
        self.assertListEqual(numpu.board, board_11)

    def test_seed_conversion(self):
        # Check if given a board, the NumPuzzle gives the right seed.
        # # Check normal NumPuzzles.
        # # # 3x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]]).seed, 0)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[0, 6, 3], [8, 5, 2], [7, 4, 1]]).seed, 362879)
        # # # 2x2 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]]).seed, 0)
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[0, 2], [3, 1]]).seed, 23)
        # # # 4x4 NumPuzzles.
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]]).seed, 0)
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[0, 12, 8, 4], [15, 11, 7, 3], [14, 10, 6, 2], [13, 9, 5, 1]]).seed, 20922789887999)
        # # Check NumPuzzles with different width and height.
        # # # 3x2 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[1, 4], [2, 5], [3, 0]]).seed, 0)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[0, 3], [5, 2], [4, 1]]).seed, 719)
        # # # 2x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[1, 3, 5], [2, 4, 0]]).seed, 0)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[0, 4, 2], [5, 3, 1]]).seed, 719)
        # # Check edge cases.
        # # # 5x1 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(5, 1), board=[[1], [2], [3], [4], [0]]).seed, 0)
        self.assertEqual(NumPuzzle(size=(5, 1), board=[[0], [4], [3], [2], [1]]).seed, 119)
        # # # 1x5 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(1, 5), board=[[1, 2, 3, 4, 0]]).seed, 0)
        self.assertEqual(NumPuzzle(size=(1, 5), board=[[0, 4, 3, 2, 1]]).seed, 119)
        # # # 1x1 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(1, 1), board=[[0]]).seed, 0)

    def test_seed_access(self):
        # Check if given a board, NumPuzzle can get the board back after converting it to a seed.
        # Build with a board, get the seed, then build with the seed and get the board.
        # # Check with normal NumPuzzles.
        # # # 3x3 NumPuzzles.
        board = [[1, 4, 7], [2, 5, 8], [3, 6, 0]]
        self.assertEqual(NumPuzzle(size=(3, 3), seed=NumPuzzle(size=(3, 3), board=board).seed).board, board)
        board = [[0, 6, 3], [8, 5, 2], [7, 4, 1]]
        self.assertEqual(NumPuzzle(size=(3, 3), seed=NumPuzzle(size=(3, 3), board=board).seed).board, board)
        # # # 2x2 NumPuzzles.
        board = [[1, 3], [2, 0]]
        self.assertEqual(NumPuzzle(size=(2, 2), seed=NumPuzzle(size=(2, 2), board=board).seed).board, board)
        board = [[0, 2], [3, 1]]
        self.assertEqual(NumPuzzle(size=(2, 2), seed=NumPuzzle(size=(2, 2), board=board).seed).board, board)
        # # # 4x4 NumPuzzles.
        board = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]]
        self.assertEqual(NumPuzzle(size=(4, 4), seed=NumPuzzle(size=(4, 4), board=board).seed).board, board)
        board = [[0, 12, 8, 4], [15, 11, 7, 3], [14, 10, 6, 2], [13, 9, 5, 1]]
        self.assertEqual(NumPuzzle(size=(4, 4), seed=NumPuzzle(size=(4, 4), board=board).seed).board, board)
        # # Check NumPuzzles with different width and height.
        # # # 3x2 NumPuzzles.
        board = [[1, 4], [2, 5], [3, 0]]
        self.assertEqual(NumPuzzle(size=(3, 2), seed=NumPuzzle(size=(3, 2), board=board).seed).board, board)
        board = [[0, 3], [5, 2], [4, 1]]
        self.assertEqual(NumPuzzle(size=(3, 2), seed=NumPuzzle(size=(3, 2), board=board).seed).board, board)
        # # # 2x3 NumPuzzles.
        board = [[1, 3, 5], [2, 4, 0]]
        self.assertEqual(NumPuzzle(size=(2, 3), seed=NumPuzzle(size=(2, 2), board=board).seed).board, board)
        board = [[0, 4, 2], [5, 3, 1]]
        self.assertEqual(NumPuzzle(size=(2, 3), seed=NumPuzzle(size=(2, 2), board=board).seed).board, board)
        # # Check edge cases.
        # # # 5x1 NumPuzzles.
        board = [[1], [2], [3], [4], [0]]
        self.assertEqual(NumPuzzle(size=(5, 1), seed=NumPuzzle(size=(5, 1), board=board).seed).board, board)
        board = [[0], [4], [3], [2], [1]]
        self.assertEqual(NumPuzzle(size=(5, 1), seed=NumPuzzle(size=(5, 1), board=board).seed).board, board)
        # # # 1x5 NumPuzzles.
        board = [[1, 2, 3, 4, 0]]
        self.assertEqual(NumPuzzle(size=(1, 5), seed=NumPuzzle(size=(1, 5), board=board).seed).board, board)
        board = [[0, 4, 3, 2, 1]]
        self.assertEqual(NumPuzzle(size=(1, 5), seed=NumPuzzle(size=(1, 5), board=board).seed).board, board)
        # # # 1x1 NumPuzzle.
        board = [[0]]
        self.assertEqual(NumPuzzle(size=(1, 1), seed=NumPuzzle(size=(1, 1), board=board).seed).board, board)


if __name__ == "__main__":
    unittest.main()

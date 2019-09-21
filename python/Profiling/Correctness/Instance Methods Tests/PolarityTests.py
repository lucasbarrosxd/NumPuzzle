# Import libraries.
import unittest
# Import from project.
# # Import implementations to test.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS

# NumPuzzle class to run tests with. Change to run tests with a different implementation.
NumPuzzle = NumPuzzleL.NumPuzzle


class PolarityTests(unittest.TestCase):
    def test_correctness(self):
        # Check if method returns correct values.
        # # Check normal NumPuzzles.
        # # # 3x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 6], [2, 0, 7], [3, 5, 8]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[0, 3, 6], [1, 4, 7], [2, 5, 8]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[0, 6, 3], [8, 5, 2], [7, 4, 1]]).polarity(), 28)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[8, 5, 3], [7, 0, 2], [6, 4, 1]]).polarity(), 28)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[8, 5, 2], [7, 4, 1], [6, 3, 0]]).polarity(), 28)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[1, 2, 3], [4, 5, 6], [7, 8, 0]]).polarity(), 9)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[1, 2, 3], [4, 0, 5], [6, 7, 8]]).polarity(), 7)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[0, 1, 2], [3, 4, 5], [6, 7, 8]]).polarity(), 9)
        # # # 2x2 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[0, 2], [1, 3]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[0, 2], [3, 1]]).polarity(), 3)
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[3, 1], [2, 0]]).polarity(), 3)
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[1, 2], [3, 0]]).polarity(), 1)
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[0, 3], [2, 1]]).polarity(), 2)
        # # # 4x4 NumPuzzles.
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]]).polarity(), 0)
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[1, 5, 8, 12], [2, 6, 9, 13], [3, 0, 10, 14], [4, 7, 11, 15]]).polarity(), 0)
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]).polarity(), 0)
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[0, 12, 8, 4], [15, 11, 7, 3], [14, 10, 6, 2], [13, 9, 5, 1]]).polarity(), 105)
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[15, 11, 7, 4], [14, 10, 0, 3], [13, 9, 6, 2], [12, 8, 5, 1]]).polarity(), 105)
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[15, 11, 7, 3], [14, 10, 6, 2], [13, 9, 5, 1], [12, 8, 4, 0]]).polarity(), 105)
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]).polarity(), 36)
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[1, 2, 3, 4], [5, 6, 7, 8], [0, 9, 10, 11], [12, 13, 14, 15]]).polarity(), 30)
        self.assertEqual(NumPuzzle(
            size=(4, 4), board=[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]).polarity(), 36)
        # # Check boards with different width and height.
        # # # 3x2 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[1, 4], [2, 5], [3, 0]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[1, 0], [2, 4], [3, 5]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[0, 3], [1, 4], [2, 5]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[0, 3], [5, 2], [4, 1]]).polarity(), 10)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[5, 3], [4, 2], [0, 1]]).polarity(), 10)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[5, 2], [4, 1], [3, 0]]).polarity(), 10)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[1, 2], [3, 4], [5, 0]]).polarity(), 3)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[1, 2], [3, 0], [4, 5]]).polarity(), 2)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[0, 1], [2, 3], [4, 5]]).polarity(), 3)
        # # # 2x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[1, 3, 5], [2, 4, 0]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[1, 0, 4], [2, 3, 5]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[0, 2, 4], [1, 3, 5]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[0, 4, 2], [5, 3, 1]]).polarity(), 10)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[5, 3, 2], [4, 0, 1]]).polarity(), 10)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[5, 3, 1], [4, 2, 0]]).polarity(), 10)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[1, 2, 3], [4, 5, 0]]).polarity(), 3)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[1, 2, 0], [3, 4, 5]]).polarity(), 1)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[0, 1, 2], [3, 4, 5]]).polarity(), 3)
        # # Check edge cases.
        # # # 3x1 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 1), board=[[1], [2], [0]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(3, 1), board=[[1], [0], [2]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(3, 1), board=[[0], [1], [2]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(3, 1), board=[[0], [2], [1]]).polarity(), 1)
        self.assertEqual(NumPuzzle(size=(3, 1), board=[[2], [0], [1]]).polarity(), 1)
        self.assertEqual(NumPuzzle(size=(3, 1), board=[[2], [1], [0]]).polarity(), 1)
        # # # 1x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(1, 3), board=[[1, 2, 0]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(1, 3), board=[[1, 0, 2]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(1, 3), board=[[0, 1, 2]]).polarity(), 0)
        self.assertEqual(NumPuzzle(size=(1, 3), board=[[0, 2, 1]]).polarity(), 1)
        self.assertEqual(NumPuzzle(size=(1, 3), board=[[2, 0, 1]]).polarity(), 1)
        self.assertEqual(NumPuzzle(size=(1, 3), board=[[2, 1, 0]]).polarity(), 1)
        # # # 1x1 NumPuzzle.
        self.assertEqual(NumPuzzle(size=(1, 1), board=[[0]]).polarity(), 0)


if __name__ == "__main__":
    unittest.main()

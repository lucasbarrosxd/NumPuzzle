# Import libraries.
import unittest
# Import from project.
# # Import implementations to test.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS

# NumPuzzle class to run tests with. Change to run tests with a different implementation.
NumPuzzle = NumPuzzleL.NumPuzzle


class DistanceHeuristicTests(unittest.TestCase):
    def test_correctness(self):
        # Check if method returns correct values.
        # # Check normal boards.
        # # # 3x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]]).distance_heuristic(), 0)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[0, 6, 3], [8, 5, 2], [7, 4, 1]]).distance_heuristic(), 20)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 0, 6]]).distance_heuristic(), 2)
        self.assertEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [0, 3, 6]]).distance_heuristic(), 4)
        # # # 2x2 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]]).distance_heuristic(), 0)
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[0, 2], [3, 1]]).distance_heuristic(), 8)
        self.assertEqual(NumPuzzle(size=(2, 2), board=[[1, 3], [0, 2]]).distance_heuristic(), 2)
        # # # 4x4 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(4, 4), board=[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]])
                         .distance_heuristic(), 0)
        self.assertEqual(NumPuzzle(size=(4, 4), board=[[0, 12, 8, 4], [15, 11, 7, 3], [14, 10, 6, 2], [13, 9, 5, 1]])
                         .distance_heuristic(), 56)
        self.assertEqual(NumPuzzle(size=(4, 4), board=[[0, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 1]])
                         .distance_heuristic(), 12)
        # # Check boards with different width and height.
        # # # 3x2 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[1, 4], [2, 5], [3, 0]]).distance_heuristic(), 0)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[0, 3], [5, 2], [4, 1]]).distance_heuristic(), 14)
        self.assertEqual(NumPuzzle(size=(3, 2), board=[[1, 4], [5, 2], [3, 0]]).distance_heuristic(), 2)
        # # # 2x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[1, 3, 5], [2, 4, 0]]).distance_heuristic(), 0)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[0, 4, 2], [5, 3, 1]]).distance_heuristic(), 14)
        self.assertEqual(NumPuzzle(size=(2, 3), board=[[1, 4, 5], [2, 3, 0]]).distance_heuristic(), 2)
        # # Check edge cases.
        # # # 3x1 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(3, 1), board=[[1], [2], [0]]).distance_heuristic(), 0)
        self.assertEqual(NumPuzzle(size=(3, 1), board=[[0], [2], [1]]).distance_heuristic(), 4)
        self.assertEqual(NumPuzzle(size=(3, 1), board=[[1], [0], [2]]).distance_heuristic(), 2)
        # # # 1x3 NumPuzzles.
        self.assertEqual(NumPuzzle(size=(1, 3), board=[[1, 2, 0]]).distance_heuristic(), 0)
        self.assertEqual(NumPuzzle(size=(1, 3), board=[[0, 2, 1]]).distance_heuristic(), 4)
        self.assertEqual(NumPuzzle(size=(1, 3), board=[[1, 0, 2]]).distance_heuristic(), 2)
        # # # 1x1 NumPuzzle
        self.assertEqual(NumPuzzle(size=(1, 1), board=[[0]]).distance_heuristic(), 0)


if __name__ == "__main__":
    unittest.main()

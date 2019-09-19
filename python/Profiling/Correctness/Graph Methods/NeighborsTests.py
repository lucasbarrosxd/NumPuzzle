# Import libraries.
import unittest
# Import from project.
# # Import implementations to test.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS

# NumPuzzle class to run tests with. Change to run tests with a different implementation.
NumPuzzle = NumPuzzleL.NumPuzzle


class NeighborsTests(unittest.TestCase):
    def test_correctness(self):
        # Check if method returns correct values.
        # # Check normal boards.
        # # # 3x3 NumPuzzles.
        # # # # Bottom-right corner.
        self.assertDictEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 0, 6]]),
                                 "L": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 0], [3, 6, 8]])
                             })
        # # # # Bottom-left corner.
        self.assertDictEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 0], [2, 5, 8], [3, 6, 7]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(3, 3), board=[[1, 0, 5], [2, 5, 8], [3, 6, 7]]),
                                 "R": NumPuzzle(size=(3, 3), board=[[1, 4, 8], [2, 5, 0], [3, 6, 7]])
                             })
        # # # # Top-left corner.
        self.assertDictEqual(NumPuzzle(size=(3, 3), board=[[0, 4, 7], [2, 5, 8], [3, 6, 1]]).neighbors(),
                             {
                                 "D": NumPuzzle(size=(3, 3), board=[[4, 0, 7], [2, 5, 8], [3, 6, 1]]),
                                 "R": NumPuzzle(size=(3, 3), board=[[2, 4, 7], [0, 5, 8], [3, 6, 1]])
                             })
        # # # # Top-right corner.
        self.assertDictEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [0, 6, 3]]).neighbors(),
                             {
                                 "D": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [6, 0, 3]]),
                                 "L": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [0, 5, 8], [2, 6, 3]])
                             })
        # # # # Top side.
        self.assertDictEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [0, 5, 8], [3, 6, 2]]).neighbors(),
                             {
                                 "R": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [3, 5, 8], [0, 6, 2]]),
                                 "D": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [5, 0, 8], [3, 6, 2]]),
                                 "L": NumPuzzle(size=(3, 3), board=[[0, 4, 7], [1, 5, 8], [3, 6, 2]])
                             })
        # # # # Left side.
        self.assertDictEqual(NumPuzzle(size=(3, 3), board=[[1, 0, 7], [2, 5, 8], [3, 6, 4]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(3, 3), board=[[0, 1, 7], [2, 5, 8], [3, 6, 4]]),
                                 "R": NumPuzzle(size=(3, 3), board=[[1, 5, 7], [2, 0, 8], [3, 6, 4]]),
                                 "D": NumPuzzle(size=(3, 3), board=[[1, 7, 0], [2, 5, 8], [3, 6, 4]])
                             })
        # # # # Bottom side.
        self.assertDictEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 0], [3, 6, 8]]).neighbors(),
                             {
                                 "L": NumPuzzle(size=(3, 3), board=[[1, 4, 0], [2, 5, 7], [3, 6, 8]]),
                                 "U": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 0, 5], [3, 6, 8]]),
                                 "R": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]])
                             })
        # # # # Right side.
        self.assertDictEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 0, 6]]).neighbors(),
                             {
                                 "L": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [0, 3, 6]]),
                                 "U": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 0, 5], [3, 6, 8]]),
                                 "R": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]])
                             })
        # # # # Center.
        self.assertDictEqual(NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 0, 8], [3, 6, 5]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [0, 2, 8], [3, 6, 5]]),
                                 "D": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 8, 0], [3, 6, 5]]),
                                 "L": NumPuzzle(size=(3, 3), board=[[1, 0, 7], [2, 4, 8], [3, 6, 5]]),
                                 "R": NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 6, 8], [3, 0, 5]])
                             })
        # # # 2x2 NumPuzzles.
        # # # # Bottom-right corner.
        self.assertDictEqual(NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(2, 2), board=[[1, 3], [0, 2]]),
                                 "L": NumPuzzle(size=(2, 2), board=[[1, 0], [2, 3]])
                             })
        # # # # Bottom-left corner.
        self.assertDictEqual(NumPuzzle(size=(2, 2), board=[[1, 0], [2, 3]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(2, 2), board=[[0, 1], [2, 3]]),
                                 "R": NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]])
                             })
        # # # # Top-left corner.
        self.assertDictEqual(NumPuzzle(size=(2, 2), board=[[0, 3], [2, 1]]).neighbors(),
                             {
                                 "D": NumPuzzle(size=(2, 2), board=[[3, 0], [2, 1]]),
                                 "R": NumPuzzle(size=(2, 2), board=[[2, 3], [0, 1]])
                             })
        # # # # Top-right corner.
        self.assertDictEqual(NumPuzzle(size=(2, 2), board=[[1, 3], [0, 2]]).neighbors(),
                             {
                                 "D": NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]]),
                                 "L": NumPuzzle(size=(2, 2), board=[[0, 3], [1, 2]])
                             })
        # # Check boards with different width and height.
        # # # 3x2 NumPuzzles.
        # # # # Bottom-right corner.
        self.assertDictEqual(NumPuzzle(size=(3, 2), board=[[1, 4], [2, 5], [3, 0]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(3, 2), board=[[1, 4], [2, 5], [0, 3]]),
                                 "L": NumPuzzle(size=(3, 2), board=[[1, 4], [2, 0], [3, 5]])
                             })
        # # # # Bottom-left corner.
        self.assertDictEqual(NumPuzzle(size=(3, 2), board=[[1, 0], [2, 5], [3, 4]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(3, 2), board=[[0, 1], [2, 5], [3, 4]]),
                                 "R": NumPuzzle(size=(3, 2), board=[[1, 5], [2, 0], [3, 4]])
                             })
        # # # # Top-left corner.
        self.assertDictEqual(NumPuzzle(size=(3, 2), board=[[0, 4], [2, 5], [3, 4]]).neighbors(),
                             {
                                 "D": NumPuzzle(size=(3, 2), board=[[4, 0], [2, 5], [3, 4]]),
                                 "R": NumPuzzle(size=(3, 2), board=[[2, 4], [0, 5], [3, 4]])
                             })
        # # # # Top-right corner.
        self.assertDictEqual(NumPuzzle(size=(3, 2), board=[[1, 4], [2, 5], [0, 3]]).neighbors(),
                             {
                                 "D": NumPuzzle(size=(3, 2), board=[[1, 4], [2, 5], [3, 0]]),
                                 "L": NumPuzzle(size=(3, 2), board=[[1, 4], [0, 5], [2, 3]])
                             })
        # # # # Top side.
        self.assertDictEqual(NumPuzzle(size=(3, 2), board=[[1, 4], [0, 5], [3, 2]]).neighbors(),
                             {
                                 "R": NumPuzzle(size=(3, 2), board=[[1, 4], [3, 5], [0, 2]]),
                                 "D": NumPuzzle(size=(3, 2), board=[[1, 4], [5, 0], [3, 2]]),
                                 "L": NumPuzzle(size=(3, 2), board=[[0, 4], [1, 5], [3, 2]])
                             })
        # # # # Bottom side.
        self.assertDictEqual(NumPuzzle(size=(3, 2), board=[[1, 4], [2, 0], [3, 5]]).neighbors(),
                             {
                                 "L": NumPuzzle(size=(3, 2), board=[[1, 0], [2, 4], [3, 5]]),
                                 "U": NumPuzzle(size=(3, 2), board=[[1, 4], [0, 2], [3, 5]]),
                                 "R": NumPuzzle(size=(3, 2), board=[[1, 4], [2, 5], [3, 0]])
                             })
        # # # 2x3 NumPuzzles.
        # # # # Bottom-right corner.
        self.assertDictEqual(NumPuzzle(size=(2, 3), board=[[1, 3, 5], [2, 4, 0]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(2, 3), board=[[1, 3, 5], [2, 0, 4]]),
                                 "L": NumPuzzle(size=(2, 3), board=[[1, 3, 0], [2, 4, 5]])
                             })
        # # # # Bottom-left corner.
        self.assertDictEqual(NumPuzzle(size=(2, 3), board=[[1, 3, 0], [2, 4, 5]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(2, 3), board=[[1, 0, 3], [2, 4, 5]]),
                                 "R": NumPuzzle(size=(2, 3), board=[[1, 3, 5], [2, 4, 0]])
                             })
        # # # # Top-left corner.
        self.assertDictEqual(NumPuzzle(size=(2, 3), board=[[0, 3, 5], [2, 4, 1]]).neighbors(),
                             {
                                 "D": NumPuzzle(size=(2, 3), board=[[3, 0, 5], [2, 4, 1]]),
                                 "R": NumPuzzle(size=(2, 3), board=[[2, 3, 5], [0, 4, 1]])
                             })
        # # # # Top-right corner.
        self.assertDictEqual(NumPuzzle(size=(2, 3), board=[[1, 3, 5], [0, 4, 2]]).neighbors(),
                             {
                                 "D": NumPuzzle(size=(2, 3), board=[[1, 3, 5], [4, 0, 2]]),
                                 "L": NumPuzzle(size=(2, 3), board=[[0, 3, 5], [1, 4, 2]])
                             })
        # # # # Left side.
        self.assertDictEqual(NumPuzzle(size=(2, 3), board=[[1, 0, 5], [2, 4, 3]]).neighbors(),
                             {
                                 "U": NumPuzzle(size=(2, 3), board=[[0, 1, 5], [2, 4, 3]]),
                                 "R": NumPuzzle(size=(2, 3), board=[[1, 4, 5], [2, 0, 3]]),
                                 "D": NumPuzzle(size=(2, 3), board=[[1, 5, 0], [2, 4, 3]])
                             })
        # # # # Right side.
        self.assertDictEqual(NumPuzzle(size=(2, 3), board=[[1, 3, 5], [2, 0, 4]]).neighbors(),
                             {
                                 "L": NumPuzzle(size=(2, 3), board=[[1, 0, 5], [2, 3, 4]]),
                                 "U": NumPuzzle(size=(2, 3), board=[[1, 3, 5], [0, 2, 4]]),
                                 "R": NumPuzzle(size=(2, 3), board=[[1, 3, 5], [2, 4, 0]])
                             })


if __name__ == "__main__":
    unittest.main()

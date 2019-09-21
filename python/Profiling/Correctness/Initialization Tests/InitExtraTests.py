# Import libraries.
import unittest
# Import from project.
# # Import implementations to test.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS

# NumPuzzle class to run tests with. Change to run tests with a different implementation.
NumPuzzle = NumPuzzleL.NumPuzzle


class InitializationExtraTests(unittest.TestCase):
    # Most initialization tests are covered in the properties.
    # Tests that aren't property specific are here.
    def test_instantiation_validation(self):
        # Check if incorrect input combination raises errors.
        # # No board, no seed and no random seed. Check multiple sizes.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 3), board=None, seed=None, random=False)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 1), board=None, seed=None, random=False)
        self.assertRaises(ValueError, NumPuzzle, size=(4, 2), board=None, seed=None, random=False)
        self.assertRaises(ValueError, NumPuzzle, size=(2, 4), board=None, seed=None, random=False)
        # Check if correct input combinations don't raise errors.
        # # Only board.
        NumPuzzle(size=(3, 3), seed=None, random=False, board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        NumPuzzle(size=(1, 1), seed=None, random=False, board=[[0]])
        NumPuzzle(size=(4, 2), seed=None, random=False, board=[[1, 5], [2, 6], [3, 7], [4, 0]])
        NumPuzzle(size=(2, 4), seed=None, random=False, board=[[1, 3, 5, 7], [2, 4, 6, 0]])
        # # Only seed.
        NumPuzzle(size=(3, 3), board=None, random=False, seed=0)
        NumPuzzle(size=(1, 1), board=None, random=False, seed=0)
        NumPuzzle(size=(4, 2), board=None, random=False, seed=0)
        NumPuzzle(size=(2, 4), board=None, random=False, seed=0)
        # # Only random.
        NumPuzzle(size=(3, 3), board=None, seed=None, random=True)
        NumPuzzle(size=(1, 1), board=None, seed=None, random=True)
        NumPuzzle(size=(4, 2), board=None, seed=None, random=True)
        NumPuzzle(size=(2, 4), board=None, seed=None, random=True)
        # # Board and seed.
        NumPuzzle(size=(3, 3), random=False, seed=0, board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        NumPuzzle(size=(1, 1), random=False, seed=0, board=[[0]])
        NumPuzzle(size=(4, 2), random=False, seed=0, board=[[1, 5], [2, 6], [3, 7], [4, 0]])
        NumPuzzle(size=(2, 4), random=False, seed=0, board=[[1, 3, 5, 7], [2, 4, 6, 0]])
        # # Board and random.
        NumPuzzle(size=(3, 3), seed=None, random=True, board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        NumPuzzle(size=(1, 1), seed=None, random=True, board=[[0]])
        NumPuzzle(size=(4, 2), seed=None, random=True, board=[[1, 5], [2, 6], [3, 7], [4, 0]])
        NumPuzzle(size=(2, 4), seed=None, random=True, board=[[1, 3, 5, 7], [2, 4, 6, 0]])
        # # Seed and random.
        NumPuzzle(size=(3, 3), board=None, seed=0, random=True)
        NumPuzzle(size=(1, 1), board=None, seed=0, random=True)
        NumPuzzle(size=(4, 2), board=None, seed=0, random=True)
        NumPuzzle(size=(2, 4), board=None, seed=0, random=True)
        # # Board, seed and random.
        NumPuzzle(size=(3, 3), seed=0, random=True, board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        NumPuzzle(size=(1, 1), seed=0, random=True, board=[[0]])
        NumPuzzle(size=(4, 2), seed=0, random=True, board=[[1, 5], [2, 6], [3, 7], [4, 0]])
        NumPuzzle(size=(2, 4), seed=0, random=True, board=[[1, 3, 5, 7], [2, 4, 6, 0]])
        # Check if solvability is correctly checked.
        # # Check on a known board.
        # # # Check if None doesn't raise errors.
        NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]], solvable=None)
        NumPuzzle(size=(2, 2), seed=0, solvable=None)
        NumPuzzle(size=(2, 2), board=[[1, 2], [3, 0]], solvable=None)
        NumPuzzle(size=(2, 2), seed=2, solvable=None)
        NumPuzzle(size=(2, 1), board=[[1], [0]], solvable=None)
        NumPuzzle(size=(2, 1), seed=0, solvable=None)
        NumPuzzle(size=(2, 1), board=[[0], [1]], solvable=None)
        NumPuzzle(size=(2, 1), seed=1, solvable=None)
        NumPuzzle(size=(1, 2), board=[[1, 0]], solvable=None)
        NumPuzzle(size=(1, 2), seed=0, solvable=None)
        NumPuzzle(size=(1, 2), board=[[0, 1]], solvable=None)
        NumPuzzle(size=(1, 2), seed=1, solvable=None)
        NumPuzzle(size=(1, 1), board=[[0]], solvable=None)
        NumPuzzle(size=(1, 1), seed=0, solvable=None)
        # # # Check if a non-solvable NumPuzzle gets rejected correctly.
        self.assertRaises(ValueError, NumPuzzle, size=(2, 2), board=[[1, 2], [3, 0]], solvable=True)
        self.assertRaises(ValueError, NumPuzzle, size=(2, 2), seed=2, solvable=True)
        self.assertRaises(ValueError, NumPuzzle, size=(3, 1), board=[[2], [1], [0]], solvable=True)
        self.assertRaises(ValueError, NumPuzzle, size=(3, 1), seed=2, solvable=True)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 3), board=[[2, 1, 0]], solvable=True)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 3), seed=2, solvable=True)
        # # # Check if a non-solvable NumPuzzle gets accepted correctly.
        NumPuzzle(size=(2, 2), board=[[1, 2], [3, 0]], solvable=False)
        NumPuzzle(size=(2, 2), seed=2, solvable=False)
        NumPuzzle(size=(3, 1), board=[[2], [1], [0]], solvable=False)
        NumPuzzle(size=(3, 1), seed=2, solvable=False)
        NumPuzzle(size=(1, 3), board=[[2, 1, 0]], solvable=False)
        NumPuzzle(size=(1, 3), seed=2, solvable=False)
        # # # Check if a solvable NumPuzzle gets rejected correctly.
        self.assertRaises(ValueError, NumPuzzle, size=(2, 2), board=[[1, 3], [2, 0]], solvable=False)
        self.assertRaises(ValueError, NumPuzzle, size=(2, 2), seed=0, solvable=False)
        self.assertRaises(ValueError, NumPuzzle, size=(3, 1), board=[[1], [2], [0]], solvable=False)
        self.assertRaises(ValueError, NumPuzzle, size=(3, 1), seed=0, solvable=False)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 3), board=[[1, 2, 0]], solvable=False)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 3), seed=0, solvable=False)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 1), board=[[0]], solvable=False)
        self.assertRaises(ValueError, NumPuzzle, size=(1, 1), seed=0, solvable=False)
        # # # Check if a solvable NumPuzzle gets accepted correctly.
        NumPuzzle(size=(2, 2), board=[[1, 3], [2, 0]], solvable=True)
        NumPuzzle(size=(2, 2), seed=0, solvable=True)
        NumPuzzle(size=(3, 1), board=[[1], [2], [0]], solvable=True)
        NumPuzzle(size=(3, 1), seed=0, solvable=True)
        NumPuzzle(size=(1, 3), board=[[1, 2, 0]], solvable=True)
        NumPuzzle(size=(1, 3), seed=0, solvable=True)
        NumPuzzle(size=(1, 1), board=[[0]], solvable=True)
        NumPuzzle(size=(1, 1), seed=0, solvable=True)

    def test_instantiation_priority(self):
        # Check if parameters have the correct precedence.
        # # Check if board has precedence over seed.
        numpu = NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]], seed=362879)
        self.assertListEqual(numpu.board, [[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        self.assertEqual(numpu.seed, 0)
        numpu = NumPuzzle(size=(3, 3), board=[[0, 6, 3], [8, 5, 2], [7, 4, 1]], seed=0)
        self.assertListEqual(numpu.board, [[0, 6, 3], [8, 5, 2], [7, 4, 1]])
        self.assertEqual(numpu.seed, 362879)
        # # Check if board has precedence over random.
        numpu = NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]], random=True)
        self.assertListEqual(numpu.board, [[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        self.assertEqual(numpu.seed, 0)
        numpu = NumPuzzle(size=(3, 3), board=[[0, 6, 3], [8, 5, 2], [7, 4, 1]], random=True)
        self.assertListEqual(numpu.board, [[0, 6, 3], [8, 5, 2], [7, 4, 1]])
        self.assertEqual(numpu.seed, 362879)
        # # Check if seed has precedence over random.
        numpu = NumPuzzle(size=(3, 3), seed=0, random=True)
        self.assertListEqual(numpu.board, [[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        self.assertEqual(numpu.seed, 0)
        numpu = NumPuzzle(size=(3, 3), seed=362879, random=True)
        self.assertListEqual(numpu.board, [[0, 6, 3], [8, 5, 2], [7, 4, 1]])
        self.assertEqual(numpu.seed, 362879)
        # # Check if board has precedence over seed and random.
        numpu = NumPuzzle(size=(3, 3), board=[[1, 4, 7], [2, 5, 8], [3, 6, 0]], seed=362879, random=True)
        self.assertListEqual(numpu.board, [[1, 4, 7], [2, 5, 8], [3, 6, 0]])
        self.assertEqual(numpu.seed, 0)
        numpu = NumPuzzle(size=(3, 3), board=[[0, 6, 3], [8, 5, 2], [7, 4, 1]], seed=0, random=True)
        self.assertListEqual(numpu.board, [[0, 6, 3], [8, 5, 2], [7, 4, 1]])
        self.assertEqual(numpu.seed, 362879)


if __name__ == '__main__':
    unittest.main()

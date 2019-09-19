# Import libraries.
import unittest
# Import from project.
# # Import implementations to test.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS

# NumPuzzle class to run tests with. Change to run tests with a different implementation.
NumPuzzle = NumPuzzleL.NumPuzzle


class SizeTests(unittest.TestCase):
    def test_instantiation_validation(self):
        # Check if incorrect sizes raise errors.
        # # Check with two invalid sizes. Check with zero and with negative sizes.
        self.assertRaises(ValueError, NumPuzzle, size=(0, 0), random=True)
        self.assertRaises(ValueError, NumPuzzle, size=(-1, 0), random=True)
        self.assertRaises(ValueError, NumPuzzle, size=(0, -1), random=True)
        self.assertRaises(ValueError, NumPuzzle, size=(-1, -1), random=True)
        # # Check with invalid width only.
        self.assertRaises(ValueError, NumPuzzle, size=(0, 3), random=True)
        self.assertRaises(ValueError, NumPuzzle, size=(-1, 3), random=True)
        # # Check with invalid height only.
        self.assertRaises(ValueError, NumPuzzle, size=(3, 0), random=True)
        self.assertRaises(ValueError, NumPuzzle, size=(3, -1), random=True)
        # # Check if valid values don't raise errors.
        NumPuzzle(size=(1, 1), random=True)
        NumPuzzle(size=(3, 3), random=True)
        NumPuzzle(size=(5, 2), random=True)
        NumPuzzle(size=(1, 7), random=True)
        NumPuzzle(size=(12, 15), random=True)

    def test_access(self):
        # Check if sizes are correctly obtained.
        numpu_1 = NumPuzzle(size=(2, 2), random=True)
        numpu_2 = NumPuzzle(size=(3, 1), random=True)
        numpu_3 = NumPuzzle(size=(1, 3), random=True)
        numpu_4 = NumPuzzle(size=(1, 1), random=True)
        # # Check when the sizes are equal.
        self.assertEqual(numpu_1.size_x, 2)
        self.assertEqual(numpu_1.size_y, 2)
        self.assertTupleEqual(numpu_1.size, (2, 2))
        # # Check when sizes are different.
        self.assertEqual(numpu_2.size_x, 3)
        self.assertEqual(numpu_2.size_y, 1)
        self.assertTupleEqual(numpu_2.size, (3, 1))

        self.assertEqual(numpu_3.size_x, 1)
        self.assertEqual(numpu_3.size_y, 3)
        self.assertTupleEqual(numpu_3.size, (1, 3))
        # Check edge cases.
        self.assertEqual(numpu_4.size_x, 1)
        self.assertEqual(numpu_4.size_y, 1)
        self.assertTupleEqual(numpu_4.size, (1, 1))


if __name__ == "__main__":
    unittest.main()

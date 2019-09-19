# Import libraries.
import unittest
# Import from project.
# # Import implementations to test.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS

# NumPuzzle class to run tests with. Change to run tests with a different implementation.
NumPuzzle = NumPuzzleL.NumPuzzle


class TextTests(unittest.TestCase):
    def test_correctness(self):
        # Check if methods returns correct values.
        # # Check normal boards.
        # # # 3x3 NumPuzzles.
        self.assertEqual(str(NumPuzzle(size=(3, 3), seed=0)),
                         "╔═╦═╦═╗\n"
                         "║1║2║3║\n"
                         "╠═╬═╬═╣\n"
                         "║4║5║6║\n"
                         "╠═╬═╬═╣\n"
                         "║7║8║ ║\n"
                         "╚═╩═╩═╝")
        self.assertEqual(str(NumPuzzle(size=(3, 3), seed=362879)),
                         "╔═╦═╦═╗\n"
                         "║ ║8║7║\n"
                         "╠═╬═╬═╣\n"
                         "║6║5║4║\n"
                         "╠═╬═╬═╣\n"
                         "║3║2║1║\n"
                         "╚═╩═╩═╝")
        # # # 2x2 NumPuzzles.
        self.assertEqual(str(NumPuzzle(size=(2, 2), seed=0)),
                         "╔═╦═╗\n"
                         "║1║2║\n"
                         "╠═╬═╣\n"
                         "║3║ ║\n"
                         "╚═╩═╝")
        self.assertEqual(str(NumPuzzle(size=(2, 2), seed=23)),
                         "╔═╦═╗\n"
                         "║ ║3║\n"
                         "╠═╬═╣\n"
                         "║2║1║\n"
                         "╚═╩═╝")
        # # # 4x4 NumPuzzles.
        self.assertEqual(str(NumPuzzle(size=(4, 4), seed=0)),
                         "╔══╦══╦══╦══╗\n"
                         "║ 1║ 2║ 3║ 4║\n"
                         "╠══╬══╬══╬══╣\n"
                         "║ 5║ 6║ 7║ 8║\n"
                         "╠══╬══╬══╬══╣\n"
                         "║ 9║10║11║12║\n"
                         "╠══╬══╬══╬══╣\n"
                         "║13║14║15║  ║\n"
                         "╚══╩══╩══╩══╝")
        self.assertEqual(str(NumPuzzle(size=(4, 4), seed=20922789887999)),
                         "╔══╦══╦══╦══╗\n"
                         "║  ║15║14║13║\n"
                         "╠══╬══╬══╬══╣\n"
                         "║12║11║10║ 9║\n"
                         "╠══╬══╬══╬══╣\n"
                         "║ 8║ 7║ 6║ 5║\n"
                         "╠══╬══╬══╬══╣\n"
                         "║ 4║ 3║ 2║ 1║\n"
                         "╚══╩══╩══╩══╝")
        # # Check NumPuzzles with different width and height.
        # # # 3x2 NumPuzzles.
        self.assertEqual(str(NumPuzzle(size=(3, 2), seed=0)),
                         "╔═╦═╦═╗\n"
                         "║1║2║3║\n"
                         "╠═╬═╬═╣\n"
                         "║4║5║ ║\n"
                         "╚═╩═╩═╝")
        self.assertEqual(str(NumPuzzle(size=(3, 2), seed=719)),
                         "╔═╦═╦═╗\n"
                         "║ ║5║4║\n"
                         "╠═╬═╬═╣\n"
                         "║3║2║1║\n"
                         "╚═╩═╩═╝")
        # # # 2x3 NumPuzzles.
        self.assertEqual(str(NumPuzzle(size=(2, 3), seed=0)),
                         "╔═╦═╗\n"
                         "║1║2║\n"
                         "╠═╬═╣\n"
                         "║3║4║\n"
                         "╠═╬═╣\n"
                         "║5║ ║\n"
                         "╚═╩═╝")
        self.assertEqual(str(NumPuzzle(size=(2, 3), seed=719)),
                         "╔═╦═╗\n"
                         "║ ║5║\n"
                         "╠═╬═╣\n"
                         "║4║3║\n"
                         "╠═╬═╣\n"
                         "║2║1║\n"
                         "╚═╩═╝")
        # # Check edge cases.
        # # # 3x1 NumPuzzles.
        self.assertEqual(str(NumPuzzle(size=(3, 1), seed=0)),
                         "╔═╦═╦═╗\n"
                         "║1║2║ ║\n"
                         "╚═╩═╩═╝")
        self.assertEqual(str(NumPuzzle(size=(3, 1), seed=5)),
                         "╔═╦═╦═╗\n"
                         "║ ║2║1║\n"
                         "╚═╩═╩═╝")
        # # # 1x3 NumPuzzles.
        self.assertEqual(str(NumPuzzle(size=(1, 3), seed=0)),
                         "╔═╗\n"
                         "║1║\n"
                         "╠═╣\n"
                         "║2║\n"
                         "╠═╣\n"
                         "║ ║\n"
                         "╚═╝")
        self.assertEqual(str(NumPuzzle(size=(1, 3), seed=5)),
                         "╔═╗\n"
                         "║ ║\n"
                         "╠═╣\n"
                         "║2║\n"
                         "╠═╣\n"
                         "║1║\n"
                         "╚═╝")
        # # # 1x1 NumPuzzle.
        self.assertEqual(str(NumPuzzle(size=(1, 1), seed=0)),
                         "╔═╗\n"
                         "║ ║\n"
                         "╚═╝")


if __name__ == "__main__":
    unittest.main()

# Importar do projeto.
from python import NumPuzzleL, NumPuzzleD, NumPuzzleS
# Importar bibliotecas.
import math
import unittest
import random


class NumPuzzleLTests(unittest.TestCase):
    NumPuzzle = NumPuzzleL.NumPuzzle

    def test_seed_basic(self):
        """Test basic operations with seed. Give a seed to NumPuzzle and try to get it back."""
        random_seed = random.randrange(math.factorial(2 * 2))
        recalculated_seed = self.NumPuzzle(size=(2, 2), seed=random_seed).seed
        self.assertEqual(random_seed, recalculated_seed)

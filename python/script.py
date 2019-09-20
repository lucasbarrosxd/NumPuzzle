import timeit
from python import NumPuzzleL, NumPuzzleS, NumPuzzleD

NumPuzzle = NumPuzzleL.NumPuzzle

# Free testing space. Run anything here.

numpu = NumPuzzle(size=(3, 3), board=[[2, 3, 7], [0, 1, 5], [4, 6, 8]])
print(numpu)

print(numpu.completeness_heuristic())
print(numpu.distance_heuristic())
print(numpu.breadth_first_search())
print(numpu.astar_search(heuristic=NumPuzzle.completeness_heuristic))
print(numpu.astar_search(heuristic=NumPuzzle.distance_heuristic))
print(numpu.heuristic_search(heuristic=NumPuzzle.completeness_heuristic))
print(numpu.heuristic_search(heuristic=NumPuzzle.distance_heuristic))

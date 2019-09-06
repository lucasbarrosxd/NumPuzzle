# Import from project.
from .AbstractNumPuzzle import AbsNumPuzzle
# Import libraries.
from typing import Optional, List


def bfs(puzzle: AbsNumPuzzle) -> Optional[List[str]]:
    discovered = {puzzle}
    puzzles = [(puzzle, None, None)]

    index = 0
    while index != len(puzzles):
        # Check if the current combination is a solution.
        if puzzles[index][0].seed == 0:
            # Solution found. Get the path to return.
            move_path = []
            while True:
                # Check if this puzzle is the starting puzzle.
                if puzzles[index][1] is not None:
                    move_path.append(puzzles[index][2])
                    index = puzzles[index][1]
                else:
                    return move_path.reverse()
        else:
            for direction, neighbor in puzzles[index][0].neighbors().items():
                if neighbor not in discovered:
                    discovered.add(neighbor)
                    puzzles.append((neighbor, index, direction))
        index += 1

    # Iterated through all reachable puzzles and didn't find solution.
    return None

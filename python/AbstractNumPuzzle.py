# Imported libraries.
from typing import Tuple, List, Dict


class AbsNumPuzzle:
    def __init__(self, size: Tuple[int, int] = (3, 3)) -> None:
        # Manually validate and set size.
        # Size will not have a setter due to it being too difficult to define a good behaviour.
        if size[0] <= 0 or size[1] <= 0:
            raise ValueError
        self._size = size

    @property
    def size(self) -> Tuple[int, int]:
        return self._size

    @property
    def size_x(self) -> int:
        return self._size[0]

    @property
    def size_y(self) -> int:
        return self._size[1]

    def __hash__(self) -> int:
        raise NotImplementedError

    def __eq__(self, other: "AbsNumPuzzle") -> bool:
        raise NotImplementedError

    def _at(self, position: Tuple[int, int]) -> int:
        raise NotImplementedError

    def _find(self, number: int) -> Tuple[int, int]:
        raise NotImplementedError

    def move(self, direction: str, to_blank: bool = True) -> None:
        raise NotImplementedError

    @property
    def seed(self) -> int:
        raise NotImplementedError

    @seed.setter
    def seed(self, value: int) -> None:
        raise NotImplementedError

    @property
    def board(self) -> List[List[int]]:
        raise NotImplementedError

    @board.setter
    def board(self, value: List[List[int]]) -> None:
        raise NotImplementedError

    def neighbors(self) -> Dict[str, "AbsNumPuzzle"]:
        raise NotImplementedError

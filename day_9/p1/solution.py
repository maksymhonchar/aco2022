import math
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class Knot:
    x: int = 0
    y: int = 0
    idx: int = 0
    path: List[Tuple[int, int]] = field(default_factory=lambda: [(0, 0)])

    def move(
        self,
        direction: str
    ) -> None:
        directions_map = {
            # ox
            'R': (1, 0),
            'L': (-1, 0),
            # oy
            'U': (0, -1),
            'D': (0, 1),
            # diagonals
            'RU': (1, -1),
            'RD': (1, 1),
            'LU': (-1, -1),
            'LD': (-1, 1)
        }
        ox_corr, oy_corr = directions_map[direction]
        self.x += ox_corr
        self.y += oy_corr
        self.path.append(
            (self.x, self.y)
        )


@dataclass
class RopeKnot(Knot):
    child: Optional[Knot] = None

    def move(
        self,
        direction: str
    ) -> None:
        super().move(direction)
        if self.child and self.is_far(self.child):
            child_direction = direction
            if (self.x > self.child.x) and (self.y < self.child.y):
                child_direction = 'RU'
            elif (self.x > self.child.x) and (self.y > self.child.y):
                child_direction = 'RD'
            elif (self.x < self.child.x) and (self.y < self.child.y):
                child_direction = 'LU'
            elif (self.x < self.child.x) and (self.y > self.child.y):
                child_direction = 'LD'
            self.child.move(child_direction)

    def is_far(
        self,
        other: Knot
    ) -> bool:
        distance = math.sqrt(
            (self.x - other.x)**2 + (self.y - other.y)**2
        )
        threshold = math.sqrt(1 + 1) + 0.00001
        return distance > threshold


def solution(
    input_file_path: str
) -> int:
    head = RopeKnot(idx=0)
    tail = RopeKnot(idx=1)
    head.child = tail

    with open(input_file_path) as fs_r:
        for command in fs_r:
            direction, steps = command.strip().split(' ')
            for _ in range(int(steps)):
                head.move(direction)

    return len(set(tail.path))

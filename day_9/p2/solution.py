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
            if self.x > self.child.x:
                child_direction = 'R'
                if self.y < self.child.y:
                    child_direction += 'U'
                elif self.y > self.child.y:
                    child_direction += 'D'
            elif self.x < self.child.x:
                child_direction = 'L'
                if self.y < self.child.y:
                    child_direction += 'U'
                elif self.y > self.child.y:
                    child_direction += 'D'
            elif self.x == self.child.x:
                if self.y < self.child.y:
                    child_direction = 'U'
                elif self.y > self.child.y:
                    child_direction = 'D'
                else:
                    raise ValueError(':)')
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


def draw_rope(
    knots: List[RopeKnot]
) -> None:
    fields = [
        str('.' * 40)
        for _ in range(40)
    ]

    start_x = start_y = len(fields) // 2

    for knot in reversed(knots):
        x, y = knot.path[-1]
        fields[start_y + y] = \
            fields[start_y + y][:start_x + x] + \
            str(knot.idx) + \
            fields[start_y + y][start_x + x + 1:]

    print('\n'.join(fields) + '\n')


def solution(
    input_file_path: str
) -> int:
    knots: List[RopeKnot] = []
    knots_count = 10

    for knot_idx in range(knots_count):
        knot = RopeKnot(idx=knot_idx)
        if knot_idx >= 1:
            knots[-1].child = knot
        knots.append(knot)

    with open(input_file_path) as fs_r:
        for command in fs_r:
            direction, steps = command.strip().split(' ')
            for _ in range(int(steps)):
                knots[0].move(direction)  # knots[0] - head

            # draw_rope(knots)
            # print('\n')

    return len(set(knots[-1].path))  # knots[-1] - tail

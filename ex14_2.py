import gzip
from dataclasses import dataclass
from math import sqrt
import sys
from pathlib import Path
from typing import Iterable, Literal, Sequence
from itertools import cycle, groupby, islice, product


def readlines() -> list[str]:
    return Path(sys.argv[1]).read_text().splitlines()


@dataclass(frozen=True)
class vec2:
    x: int
    y: int

    @staticmethod
    def xs(vecs: Iterable["vec2"]) -> list[int]:
        return [vec.x for vec in vecs]

    @staticmethod
    def ys(vecs: Iterable["vec2"]) -> list[int]:
        return [vec.y for vec in vecs]

    @staticmethod
    def all_directions() -> list["vec2"]:
        return [
            vec2(x, y) for x, y in product([+1, -1, 0], repeat=2) if (x, y) != (0, 0)
        ]

    @staticmethod
    def cardinal_directions() -> list["vec2"]:
        return [vec2(x, y) for x, y in ((+1, 0), (-1, 0), (0, -1), (0, +1))]

    def __add__(self, other: "vec2") -> "vec2":
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "vec2") -> "vec2":
        return vec2(self.x - other.x, self.y - other.y)

    def __neg__(self) -> "vec2":
        return vec2(-self.x, -self.y)

    def euclidean(self, other: "vec2") -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def manhattan(self, other: "vec2") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def all_neighbors(self) -> list["vec2"]:
        return [self + delta for delta in vec2.all_directions()]

    def cardinal_neighbors(self) -> list["vec2"]:
        return [self + delta for delta in vec2.cardinal_directions()]


def parse_line(line: str) -> tuple[vec2, vec2]:
    p, v = line.strip().split()
    p = vec2(*map(int, p.split("=")[-1].split(",")))
    v = vec2(*map(int, v.split("=")[-1].split(",")))
    return p, v


robots = [parse_line(line) for line in readlines()]

BOUNDS = (11, 7) if len(robots) < 30 else (101, 103)


def move(pos: vec2, vel: vec2) -> vec2:
    new_pos = pos + vel
    return vec2(new_pos.x % BOUNDS[0], new_pos.y % BOUNDS[1])


def make_grid(robots: list[vec2]) -> str:
    grid: list[list[str]] = []
    for y in range(BOUNDS[1]):
        row = [" "] * BOUNDS[0]
        grid.append(row)
    for pos in robots:
        grid[pos.y][pos.x] = "#"
    return "\n".join("".join(row) for row in grid)


frames = []
frame_compressed_lengths = [0] * 10_000
seconds = 0
for i in range(10_000):
    frame_compressed_lengths[i] = len(
        gzip.compress(bytearray([pos.x for pos, _ in robots]))
    ) + len(gzip.compress(bytearray([pos.y for pos, _ in robots])))
    frames.append([pos for pos, _ in robots])
    robots = [(move(pos, vel), vel) for pos, vel in robots]
    seconds += 1

tree_frame_num = min(enumerate(frame_compressed_lengths), key=lambda x: x[1])[0]

print(make_grid(frames[tree_frame_num]))
print(tree_frame_num)

from collections import deque, defaultdict
from functools import lru_cache

stones = deque([])

with open("in11.txt", "r") as f:
    for line in f:
        stones.extend([int(c) for c in line.split(" ") if c != "\n"])


@lru_cache(maxsize=None)
def dfs(v, remaining):
    if remaining == 0:
        return 1

    res = 0
    if v == 0:
        res = dfs(1, remaining - 1)
    elif len(str(v)) % 2 == 0:
        tmp = str(v)
        midpoint = len(tmp) // 2
        a = tmp[:midpoint]
        b = tmp[midpoint:].lstrip("0")
        res = dfs(int(a), remaining - 1)
        res += dfs(int(b) if b else 0, remaining - 1)
    else:
        res = dfs(v * 2024, remaining - 1)
    return res


res = 0
for v in stones:
    res += dfs(v, 75)
print(res)

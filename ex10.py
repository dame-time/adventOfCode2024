from collections import deque, defaultdict

grid = []

with open("in10.txt", "r") as f:
    for line in f:
        grid += [[int(v) for v in line if v != "\n"]]

n, m = len(grid), len(grid[0])
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque()
res = defaultdict(int)
visited = set()
tot = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] == 0:
            visited.add((r, c))
            res[(r, c)] += 1
            q.append((r, c))

while q:
    i, j = q.popleft()
    currV = grid[i][j]

    if currV == 9:
        tot += res[(i, j)]
        continue

    for d0, d1 in dirs:
        x, y = i + d0, j + d1
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != currV + 1:
            continue

        if (x, y) in visited:
            res[(x, y)] += res[(i, j)]
            continue

        visited.add((x, y))
        res[(x, y)] += res[(i, j)]
        q.append((x, y))
print(tot)

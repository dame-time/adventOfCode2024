from collections import deque

map = []

with open("in6.txt", "r") as f:
    for line in f:
        map += [[c for c in line if c != "\n"]]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
q = deque()

n, m = len(map), len(map[0])
start = None
for i in range(n):
    for j in range(m):
        if map[i][j] == "^":
            start = (i, j, 0)
            break

q = deque([(start[0], start[1], 0)])
path = set()
while q:
    i, j, d = q.popleft()
    x, y = dirs[d]

    path.add((i, j))
    if i + x < 0 or i + x >= n or j + y < 0 or j + y >= m:
        break

    if map[i + x][j + y] == "#" or map[i + x][j + y] == "O":
        q.append((i, j, (d + 1) % len(dirs)))
    else:
        q.append((i + x, j + y, d))


res = 0
for r, c in path:
    if (r, c, 0) == start:
        continue
    q = deque([(start[0], start[1], 0)])
    valid = False
    visited = set([(start[0], start[1], 0)])
    map[r][c] = "#"
    while q:
        i, j, d = q.popleft()
        x, y = dirs[d]

        if i + x < 0 or i + x >= n or j + y < 0 or j + y >= m:
            valid = True
            break

        if (i + x, j + y, d) in visited:
            valid = False
            break

        if map[i + x][j + y] == "#":
            visited.add((i, j, (d + 1) % len(dirs)))
            q.append((i, j, (d + 1) % len(dirs)))
        else:
            visited.add((i + x, j + y, d))
            q.append((i + x, j + y, d))
    if not valid:
        res += 1
    map[r][c] = "."

print(res)

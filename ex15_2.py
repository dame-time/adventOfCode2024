from collections import deque
import copy

n, m = 0, 0
grid = []
moves = []

dirs = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}

with open("in15.txt", "r") as f:
    tmp = []
    for line in f:
        if line == "\n":
            grid = copy.deepcopy(tmp)
            n, m = len(grid), len(grid[0])
            tmp = []
            continue
        tmp += [[c for c in line if c != "\n"]]
    moves = copy.deepcopy(tmp)

moves = [dirs[col] for row in moves for col in row]
wall, obstacle, robot = "#", "O", "@"
start = None

tmp = copy.deepcopy(grid)
for i in range(n):
    for j in range(m):
        if tmp[i][j] == robot:
            grid[i][j] = "@."
        elif tmp[i][j] == obstacle:
            grid[i][j] = "[]"
        elif tmp[i][j] == wall:
            grid[i][j] = "##"
        else:
            grid[i][j] = ".."

grid = [[char for cell in row for char in cell] for row in grid]
n, m = len(grid), len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] == robot:
            start = [i, j]
            break

# for row in grid:
#     print(row)

obstacles = set(["[", "]"])


def getFullObstacle(i, j):
    try:
        if grid[i][j] not in obstacles:
            return []
    except:
        for row in grid:
            print(row)

    if grid[i][j] == "[":
        return [(i, j), (i, j + 1)]
    return [(i, j), (i, j - 1)]


def getAllObstaclesInRange(obstacle, d):
    visited = obstacle
    q = deque(obstacle)
    while q:
        i, j = q.popleft()
        x, y = i + d[0], j + d[1]
        for obst in getFullObstacle(x, y):
            if obst not in visited:
                visited.append(obst)
                q.append(obst)
    return visited


for r, c in moves:
    x, y = start[0] + r, start[1] + c
    stack = [tuple(start)]
    stack += getAllObstaclesInRange(getFullObstacle(x, y), (r, c))

    areWallsPresent = False
    for v in stack:
        if grid[v[0] + r][v[1] + c] == wall:
            areWallsPresent = True
            break

    if areWallsPresent:
        continue

    while stack:
        i, j = stack.pop()
        grid[i][j], grid[i + r][j + c] = grid[i + r][j + c], grid[i][j]
        if not stack:
            start = [i + r, j + c]

for row in grid:
    print(row)

res = 0
visited = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] in obstacles:
            obst = getFullObstacle(i, j)

            if obst[0] in visited or obst[1] in visited:
                continue

            visited.add(obst[0])
            visited.add(obst[1])
            minX = min(obst[0][1], obst[1][1])
            res += (i * 100) + minX
    # print(grid[i])
print(res)

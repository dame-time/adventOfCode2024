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

for i in range(n):
    for j in range(m):
        if grid[i][j] == robot:
            start = [i, j]
            break

# print(grid)
# print(moves)

for r, c in moves:
    x, y = start[0] + r, start[1] + c
    stack = [start]

    while grid[x][y] == obstacle:
        stack += [(x, y)]
        x += r
        y += c

    if grid[x][y] == wall:
        continue

    while stack:
        i, j = stack.pop()
        grid[i][j], grid[i + r][j + c] = grid[i + r][j + c], grid[i][j]
        if not stack:
            start = [i + r, j + c]

res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == obstacle:
            res += (i * 100) + j
    print(grid[i])
print(res)

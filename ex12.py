from collections import deque

grid = []

with open("in12.txt", "r") as f:
    for line in f:
        grid += [[c for c in line if c != "\n"]]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = len(grid), len(grid[0])
visited = set()
res = 0


def neighbourhood(p):
    neighbourhood = [
        [False, False, False],
        [False, False, False],
        [False, False, False],
    ]
    idx = grid[p[0]][p[1]]
    for row_index in range(3):
        for col_index in range(3):
            r, c = p[0] - 1 + row_index, p[1] - 1 + col_index
            if 0 <= r < n and 0 <= c < m and grid[r][c] == idx:
                neighbourhood[row_index][col_index] = True
    return neighbourhood


def count_corners(neighbourhood):
    count = 0
    if not neighbourhood[1][0] and not neighbourhood[0][1]:
        count += 1
    if not neighbourhood[0][0] and neighbourhood[1][0] and neighbourhood[0][1]:
        count += 1
    if not neighbourhood[1][2] and not neighbourhood[0][1]:
        count += 1
    if not neighbourhood[0][2] and neighbourhood[1][2] and neighbourhood[0][1]:
        count += 1
    if not neighbourhood[1][0] and not neighbourhood[2][1]:
        count += 1
    if not neighbourhood[2][0] and neighbourhood[1][0] and neighbourhood[2][1]:
        count += 1
    if not neighbourhood[1][2] and not neighbourhood[2][1]:
        count += 1
    if not neighbourhood[2][2] and neighbourhood[1][2] and neighbourhood[2][1]:
        count += 1
    return count


for r in range(n):
    for c in range(m):
        if (r, c) in visited:
            continue

        curr = grid[r][c]
        visited.add((r, c))
        sides = []
        corners = 0
        area = 0
        q = deque([(r, c)])
        while q:
            i, j = q.popleft()
            area += 1

            cell_neighbourhood = neighbourhood((i, j))
            corners += count_corners(cell_neighbourhood)

            for h, v in dirs:
                x, y = i + h, j + v
                if (
                    x < 0
                    or x >= n
                    or y < 0
                    or y >= m
                    or grid[x][y] != curr
                    or (x, y) in visited
                ):
                    continue

                visited.add((x, y))
                q.append((x, y))

        res += area * corners

print(res)

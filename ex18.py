from collections import deque

coords = []

with open("in18.txt", "r") as f:
    for line in f:
        line = "".join([c for c in line if c != "\n"])
        coords += [[int(v) for v in line.split(",")]]

n = 71
toSim = 1024


def dijkstra(charToSim):
    grid = [["." for _ in range(n)] for _ in range(n)]

    for i in range(charToSim):
        grid[coords[i][1]][coords[i][0]] = "#"

    end = (n - 1, n - 1)
    q = deque([(0, 0, 0)])
    visited = {(i, j): float("inf") for i in range(n) for j in range(n)}
    visited[(0, 0)] = 0
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        steps, i, j = q.popleft()
        for d0, d1 in dirs:
            x, y = i + d0, j + d1
            if (
                x < 0
                or x >= n
                or y < 0
                or y >= n
                or grid[x][y] == "#"
                or visited[(x, y)] <= steps + 1
            ):
                continue
            visited[(x, y)] = steps + 1
            q.append((steps + 1, x, y))

    return visited[end]


start = toSim
end = len(coords)
while start < end:
    mid = (start + end) // 2
    if dijkstra(mid) == float("inf"):
        end = mid - 1
    else:
        start = mid + 1
print(coords[start])

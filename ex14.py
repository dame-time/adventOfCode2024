from collections import deque

n, m = 103, 101
grid = [[set() for _ in range(m)] for _ in range(n)]

robots = {}
with open("in14.txt", "r") as f:
    for line in f:
        tmp = line.split(" ")
        pos = [int(v) for v in tmp[0][2:].split(",")][::-1]
        vel = [int(v) for v in tmp[1][2:].split(",")][::-1]
        grid[pos[0]][pos[1]].add(len(robots))
        robots[len(robots)] = [pos, vel]

for i in range(100):
    for key in robots.keys():
        pos, vel = robots[key]
        grid[pos[0]][pos[1]].remove(key)
        pos[0] += vel[0]
        pos[1] += vel[1]
        if pos[0] < 0:
            pos[0] = n + pos[0]
        elif pos[0] >= n:
            pos[0] %= n
        if pos[1] < 0:
            pos[1] = m + pos[1]
        elif pos[1] >= m:
            pos[1] %= m
        robots[key] = [pos, vel]
        grid[pos[0]][pos[1]].add(key)


def printGrid():
    res = []
    for row in grid:
        curr = []
        for v in row:
            curr += [str(len(v))]
        res += [curr]

    for i in range(len(res)):
        tmp = ""
        if i == n // 2:
            print("")
            continue

        for j in range(len(res[i])):
            if j == m // 2:
                tmp += " "
                continue
            tmp += str(res[i][j])
        print(tmp)


def computeRes():
    res = []
    for row in grid:
        curr = []
        for v in row:
            curr += [len(v)]
        res += [curr]

    halfX, halfY = n // 2, m // 2
    startPoints = [(0, 0), (halfX + 1, 0), (0, halfY + 1), (halfX + 1, halfY + 1)]
    dirs = [(1, 0), (0, 1)]
    tot = 1
    for p in startPoints:
        q = deque([p])
        visited = set()
        visited.add(p)
        s = 0
        while q:
            i, j = q.popleft()
            s += res[i][j]
            for d0, d1 in dirs:
                x, y = i + d0, j + d1
                if x < 0 or x >= n or y < 0 or y >= m or x == halfX or y == halfY:
                    continue

                if (x, y) in visited:
                    continue

                visited.add((x, y))
                q.append((x, y))
        tot *= s
    print(tot)


printGrid()
computeRes()

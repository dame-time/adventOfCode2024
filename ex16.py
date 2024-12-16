import heapq
from collections import defaultdict

grid = []
wall = "#"

with open("in16.txt", "r") as f:
    for line in f:
        grid += [[c for c in line if c != "\n"]]

n, m = len(grid), len(grid[0])
walkCost = 1
rotCost = 1000
dirs = {
    (0, 1): [(1, 0), (-1, 0)],
    (0, -1): [(1, 0), (-1, 0)],
    (1, 0): [(0, 1), (0, -1)],
    (-1, 0): [(0, 1), (0, -1)],
}

start = None
end = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "E":
            end = (i, j)


def dijkstra():
    dists = defaultdict(lambda: float("inf"))
    parents = defaultdict(set)

    initial_state = (start, (0, 1))
    dists[initial_state] = 0

    heap = [(0, start, (0, 1))]

    while heap:
        cost, pos, currDir = heapq.heappop(heap)

        i, j = pos[0] + currDir[0], pos[1] + currDir[1]
        if 0 <= i < n and 0 <= j < m and grid[i][j] != wall:
            new_cost = cost + walkCost
            next_state = ((i, j), currDir)
            old_cost = dists[next_state]
            if new_cost < old_cost:
                # Found better path, resetting my parent
                dists[next_state] = new_cost
                parents[next_state] = {(pos, currDir)}
                heapq.heappush(heap, (new_cost, (i, j), currDir))
            elif new_cost == old_cost:
                # Equally good path found
                parents[next_state].add((pos, currDir))

        for nxtDir in dirs[currDir]:
            i, j = pos[0] + nxtDir[0], pos[1] + nxtDir[1]
            if 0 <= i < n and 0 <= j < m and grid[i][j] != wall:
                new_cost = cost + walkCost + rotCost
                next_state = ((i, j), nxtDir)
                old_cost = dists[next_state]
                if new_cost < old_cost:
                    # Found better path, resetting my parent
                    dists[next_state] = new_cost
                    parents[next_state] = {(pos, currDir)}
                    heapq.heappush(heap, (new_cost, (i, j), nxtDir))
                elif new_cost == old_cost:
                    # Equally good path
                    parents[next_state].add((pos, currDir))

    return dists, parents


def backtrack_all_paths(parents, start_state, end_pos):
    end_states = [s for s in parents.keys() if s[0] == end_pos]
    all_paths = []
    for end_state in end_states:
        all_paths.extend(dfs(parents, start_state, end_state))
    return all_paths


def dfs(parents, s, curr):
    if curr == s:
        return [[curr]]
    paths = []
    for p in parents[curr]:
        for path in dfs(parents, s, p):
            paths.append(path + [curr])
    return paths


dists, parents = dijkstra()

initial_state = (start, (0, 1))
all_paths = backtrack_all_paths(parents, initial_state, end)

unique_positions_across_all_paths = set()
for path in all_paths:
    for pos, direction in path:
        unique_positions_across_all_paths.add(pos)

count_unique_nodes = len(unique_positions_across_all_paths)
print("Number of unique nodes in all minimal paths:", count_unique_nodes)

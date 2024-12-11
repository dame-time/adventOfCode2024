from collections import deque, defaultdict

mat = []
validLetters = {"X", "M", "A", "S"}

with open("in4.txt", "r") as f:
    for line in f:
        mat += [[c for c in line if c != "\n"]]

dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
n, m = len(mat), len(mat[0])
res = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == "A":
            freq = defaultdict(list)
            for x, y in dirs:
                if 0 <= i + x < n and 0 <= j + y < m:
                    freq[mat[i + x][j + y]] += [(i + x, j + y)]
            if len(freq["M"]) == 2 and len(freq["S"]) == 2:
                print(freq)
                if (
                    freq["M"][0][0] == freq["M"][1][0]
                    or freq["M"][0][1] == freq["M"][1][1]
                ):
                    res += 1

print(res)

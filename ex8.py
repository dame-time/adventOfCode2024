from collections import defaultdict

mat = []
antennas = defaultdict(list)

with open("in8.txt", "r") as f:
    for line in f:
        mat += [[c for c in line if c != "\n"]]

n, m = len(mat), len(mat[0])

antinodes = set()
for i in range(n):
    for j in range(m):
        if mat[i][j] != ".":
            antinodes.add((i, j))
            antennas[mat[i][j]] += [(i, j)]

for k in antennas.keys():
    tmp = antennas[k]
    tmp.sort(key=lambda x: x[1])
    print(tmp)
    for i in range(len(tmp)):
        for j in range(i + 1, len(tmp)):
            xDiff = abs(tmp[i][0] - tmp[j][0])
            yDiff = abs(tmp[i][1] - tmp[j][1])
            if tmp[i][0] < tmp[j][0]:
                topX, topY = (tmp[i][0] - xDiff, tmp[i][1] - yDiff)
                botX, botY = (tmp[j][0] + xDiff, tmp[j][1] + yDiff)
                while 0 <= topX < n and 0 <= topY < m:
                    mat[topX][topY] = "#"
                    antinodes.add((topX, topY))
                    topX -= xDiff
                    topY -= yDiff
                while 0 <= botX < n and 0 <= botY < m:
                    mat[botX][botY] = "#"
                    antinodes.add((botX, botY))
                    botX += xDiff
                    botY += yDiff
            else:
                topX, topY = (tmp[i][0] + xDiff, tmp[i][1] - yDiff)
                botX, botY = (tmp[j][0] - xDiff, tmp[j][1] + yDiff)
                while 0 <= topX < n and 0 <= topY < m:
                    mat[topX][topY] = "#"
                    antinodes.add((topX, topY))
                    topX += xDiff
                    topY -= yDiff
                while 0 <= botX < n and 0 <= botY < m:
                    mat[botX][botY] = "#"
                    antinodes.add((botX, botY))
                    botX -= xDiff
                    botY += yDiff

for row in mat:
    print(row)
print(antinodes)
print(len(antinodes))

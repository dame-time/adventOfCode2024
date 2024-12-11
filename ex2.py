m = []

with open("in2.txt", "r") as f:
    for line in f:
        row = line.split(" ")
        m.append([int(num) for num in row])


def dfs(seq, i, tmp, dampener, currDir):
    if len(tmp) >= len(seq) - 1:
        return True

    if i >= len(seq):
        return False

    res = False
    if not tmp or 1 <= (seq[i] - tmp[-1]) * currDir <= 3:
        res = res or dfs(seq, i + 1, tmp + [seq[i]], dampener, currDir)
    elif dampener >= 1:
        res = res or dfs(seq, i + 1, tmp, dampener - 1, currDir)
        tmp.pop()
        if not tmp or 1 <= (seq[i] - tmp[-1]) * currDir <= 3:
            res = res or dfs(seq, i + 1, tmp + [seq[i]], dampener - 1, currDir)
    return res


res = 0
for row in m:
    currDir = -1 if row[0] > row[1] else 1
    safe = dfs(row, 0, [], 1, currDir) or dfs(row, 0, [], 1, -currDir)
    res += 1 if safe else 0

print(res)

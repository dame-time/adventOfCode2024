from functools import cache

availTowels = []
desiredComb = []

with open("in19.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            availTowels = [
                "".join([c for c in v if c != "\n" and c != ","])
                for v in line.split(" ")
            ]
        elif i > 1:
            desiredComb += ["".join([c for c in line if c != "\n"])]


@cache
def dfs(i, target):
    if i >= len(target):
        return 1

    res = 0
    for v in availTowels:
        if target[i:].startswith(v):
            res += dfs(i + len(v), target)
    return res


res = 0
for comb in desiredComb:
    res += dfs(0, comb)
print(res)

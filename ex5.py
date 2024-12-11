from collections import defaultdict, deque

graph = defaultdict(set)

check = []

with open("in5.txt", "r") as f:
    for line in f:
        if "|" in line:
            node0, node1 = line.split("|")
            node0, node1 = int(node0), int(node1)
            graph[node0].add(node1)
        else:
            tmp = [int(v) for v in line.split(",") if v != " " and v != "\n"]
            if tmp:
                check += [tmp]

res = 0
for row in check:
    wasInvalid = None
    while True:
        valid = True
        for i in range(1, len(row)):
            if row[i - 1] in graph[row[i]]:
                row[i], row[i - 1] = row[i - 1], row[i]
                valid = False
        if valid:
            break
        wasInvalid = True
    if wasInvalid:
        res += row[len(row) // 2]

print(res)

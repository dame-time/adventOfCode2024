from collections import deque
from sortedcontainers import SortedList

s = ""

with open("in9.txt", "r") as f:
    for line in f:
        s += line

stack = []
ids = []
lastId = 0
for i in range(len(s)):
    if i % 2 == 0 or i == 0:
        tmp = [len(stack), str(lastId), 0]
        for j in range(int(s[i])):
            stack += [str(lastId)]
            tmp[-1] += 1
        ids += [tmp]
        lastId += 1
    else:
        for j in range(int(s[i])):
            stack += ["."]

for i in range(len(ids) - 1, -1, -1):
    pos = -1
    j = 0
    while j < len(stack):
        count = 0
        start = j
        while j < len(stack) and stack[j] == ".":
            count += 1
            j += 1
        if count >= ids[i][-1] and start < ids[i][0]:
            pos = start
            break
        j += 1
    if pos >= 0:
        for k in range(ids[i][-1]):
            stack[ids[i][0] + k] = "."

        ids[i][0] = pos

        for k in range(ids[i][-1]):
            stack[ids[i][0] + k] = ids[i][1]


checksum = 0
for v in ids:
    startId = v[0]
    for j in range(v[2]):
        checksum += startId * int(v[1])
        startId += 1

print(checksum)

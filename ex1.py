from collections import defaultdict

freqLeft = []
rightFreq = defaultdict(int)

with open("in1.txt", "r") as file:
    for line in file:
        tmp = line.split(" ")
        freqLeft.append(int(tmp[0]))
        rightFreq[int(tmp[-1])] += 1

res = 0
for v in freqLeft:
    res += v * rightFreq[v]

print(res)

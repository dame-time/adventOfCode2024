from collections import deque

equations = []

with open("in7.txt", "r") as f:
    for line in f:
        tmp = [c for c in line.split(" ") if c != "\n"]
        tmp[0] = tmp[0][:-1]
        if "\n" in tmp[-1]:
            tmp[-1] = tmp[-1][:-1]
        equations += [[c for c in tmp]]

op = ["+", "*", "||"]


def evaluate(eq):
    eq = deque(eq)
    while len(eq) > 1:
        curr = 0
        if eq[1] == "+":
            curr = int(eq[0]) + int(eq[2])
        elif eq[1] == "*":
            curr = int(eq[0]) * int(eq[2])
        else:
            curr = int(str(eq[0]) + str(eq[2]))
        eq.popleft()
        eq.popleft()
        eq.popleft()
        eq.appendleft(curr)
    return eq[0]


def dfs(l, i, tmp):
    if i >= len(l) - 1:
        tmp += [l[i]]
        return evaluate(tmp) == int(l[0])

    res = False
    for operator in op:
        res = res or dfs(l, i + 1, tmp + [l[i], operator])
    return res


res = 0
for eq in equations:
    if dfs(eq, 1, []):
        print(eq)
        res += int(eq[0])

print(res)

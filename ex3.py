from collections import defaultdict, deque

s = ""

with open("in3.txt", "r") as f:
    for line in f:
        s += line

validChars = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "(", ")"}
enabled = True

i = 0
res = 0
while i < len(s):
    c = s[i]
    if c == "m" and s[i : i + 3] == "mul":
        if i + 3 >= len(s):
            i += 1
            continue

        i += 3

        if not enabled:
            continue

        stack = deque([])
        freq = defaultdict(int)
        while i < len(s) and s[i] in validChars:
            if s[i] == ")":
                stack += [s[i]]
                freq[s[i]] += 1
                i += 1
                break
            stack += [s[i]]
            freq[s[i]] += 1
            i += 1

        if (
            freq[","] != 1
            or freq["("] != 1
            or freq[")"] != 1
            or stack[0] != "("
            or stack[-1] != ")"
        ):
            continue

        stack.pop()
        stack.popleft()
        values = "".join(stack).split(",")
        if len(values) != 2:
            continue

        print(values)
        res += int(values[0]) * int(values[1])
        continue

    if c == "d" and s[i : i + 4] == "do()":
        enabled = True
        print(s[i : i + 4])
        i += 4
        continue
    elif c == "d" and s[i : i + 7] == "don't()":
        enabled = False
        print(s[i : i + 7])
        i += 7
        continue
    i += 1

print(res)

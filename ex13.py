from fractions import Fraction
from functools import lru_cache

prizes = []

with open("in13.txt", "r") as f:
    tmp = []
    ignore = {"X", "Y", "\n", "+", "="}
    for line in f:
        if line == "\n":

            if not tmp:
                continue

            prizes += [tmp]
            tmp = []
            continue
        values = line.split(" ")
        y = "".join([c for c in values[-1] if c not in ignore])
        x = "".join([c for c in values[-2][:-1] if c not in ignore])
        tmp += [(int(x), int(y))]

    if tmp:
        prizes += [tmp]

costX = 3
costY = 1


print(prizes)


def is_near_integer(value):
    return value.denominator == 1


tot = 0
for prize in prizes:
    a, c = prize[0]
    b, d = prize[1]
    t0, t1 = prize[2]

    t0 += 10000000000000
    t1 += 10000000000000

    try:
        x = Fraction(t0) - Fraction(b * t1, d)
        x /= Fraction(a) - Fraction(b * c, d)

        y = Fraction(t1) - Fraction(c) * x
        y /= Fraction(d)

        if (
            is_near_integer(x)
            and is_near_integer(y)
            and x.numerator >= 0
            and y.numerator >= 0
        ):
            tot += (x.numerator * costX) + (y.numerator * costY)
            print((x.numerator, y.numerator))
            print(x, y, prize)
    except ZeroDivisionError:
        print("Div by 0")
print(tot)

import math


def solve(piles, h):
    l, r = 1, max(piles)
    res = r
    while l <= r:
        k = (l + r) // 2
        s = 0
        for x in piles:
            s += math.ceil(x / k)

        if s <= h:
            res = k
            r = k - 1
        elif s > h:
            l = k + 1
    return res


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(solve(piles, h))

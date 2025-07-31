from collections import defaultdict


def solve(s, k):
    l = 0
    count = defaultdict(int)
    res = 1
    maxf = 0

    for r in range(len(s)):
        count[s[r]] += 1
        maxf = max(maxf, count[s[r]])
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    print(solve(s, k))

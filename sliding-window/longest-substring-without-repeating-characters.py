def solve(s):
    res = 0
    remember = {}
    l = 0

    for i in range(len(s)):
        c = s[i]
        if c in remember:
            l = max(l, remember[c] + 1)
        remember[c] = i
        res = max(res, i - l + 1)
    return res


if __name__ == "__main__":
    s = "abcabcbb"
    print(solve(s))

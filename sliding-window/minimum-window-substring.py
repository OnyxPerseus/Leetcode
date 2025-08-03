from collections import defaultdict


def solve(s, t):
    m = len(s)
    n = len(t)
    if m < n:
        return ""
    res = (-1, -1)
    resLength = float("inf")
    countA = defaultdict(int)
    countB = defaultdict(int)
    l = 0
    have = 0

    for i in range(n):
        countB[t[i]] += 1

    need = len(countB)
    for r in range(m):
        countA[s[r]] += 1
        if s[r] in countB and countB[s[r]] == countA[s[r]]:
            have += 1

        while have == need:
            if resLength > r - l + 1:
                res = (l, r)
                resLength = r - l + 1
            if s[l] in countB and countB[s[l]] == countA[s[l]]:
                have -= 1
            countA[s[l]] -= 1
            l += 1
    return s[res[0] : res[1] + 1] if resLength != float("inf") else ""


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solve(s, t))  # Output: "BANC"

from collections import defaultdict


def solve(s, t):
    if len(s) != len(t):
        return False

    count = defaultdict(int)
    for c in s:
        count[c] += 1
    for c in t:
        if count[c] == 0:
            return False
        count[c] -= 1
    return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(solve(s, t))

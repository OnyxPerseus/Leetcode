from collections import defaultdict


def solve(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[','.join(map(lambda x: str(x),count))].append(s)

    return list(res.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solve(strs))

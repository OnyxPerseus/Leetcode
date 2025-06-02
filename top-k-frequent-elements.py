from collections import defaultdict


def solve(nums, k):
    res = []
    n = len(nums)
    count = defaultdict(int)
    buckets = [[] for _ in range(n+1)]

    for x in nums:
        count[x] += 1

    for key, value in count.items():
        buckets[value].append(key)
    
    time = 0
    for i in range(n, -1, -1):
        for x in buckets[i]:
            res.append(x)
            time+=1
            if time >= k:
                return res
    return res


if __name__ == "__main__":
    nums = [1]
    k = 1
    print(solve(nums, k))

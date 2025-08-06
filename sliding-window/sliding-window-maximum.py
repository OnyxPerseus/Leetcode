from collections import deque


def solve(nums, k):
    n = len(nums)
    if n == 1:
        return [nums[0]]

    res = []
    queue = deque()
    l = 0

    for r in range(n):
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        queue.append(r)

        if l > queue[0]:
            queue.popleft()

        if r + 1 >= k:
            res.append(nums[queue[0]])
            l += 1
    return res


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(solve(nums, k))

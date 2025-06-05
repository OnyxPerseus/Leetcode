def solve(nums):
    res = 0
    remember = set(nums)
    for x in remember:
        if x - 1 not in remember:
            length = 1
            while x + length in remember:
                length += 1
            res = max(res, length)
    return res


if __name__ == "__main__":
    nums = [1, 0, 1, 2]
    print(solve(nums))

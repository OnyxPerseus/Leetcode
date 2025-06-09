def solve(nums):
    n = len(nums)
    res = []
    nums.sort()
    for i, x in enumerate(nums):
        if x > 0:  # because the array is sorted by asc
            break

        if i > 0 and x == nums[i - 1]:
            continue

        l, r = i + 1, n - 1
        while l < r:
            if x + nums[l] + nums[r] > 0:
                r -= 1
            elif x + nums[l] + nums[r] < 0:
                l += 1
            else:
                res.append([x, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l - 1] == nums[l] and l < r:
                    l += 1
    return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(solve(nums))

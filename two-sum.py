def solve(nums, target):
    remember = {}
    for [i, x] in enumerate(nums):
        y = target - x
        if y in remember:
            return [i, remember[y]]
        remember[x] = i
    return [-1, -1]


if __name__ == "__main__":
    # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    # You can return the answer in any order.
    nums = [2, 7, 11, 15]
    target = 9
    print(solve(nums, target))

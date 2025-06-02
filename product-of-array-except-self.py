def solve(nums):
    n = len(nums)
    result = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

if __name__ == "__main__":
    """
        Input: nums = [1,2,3,4]
        [1,1,2,6]
        [24,12,4,1]
        Output: [24,12,8,6]
    """
    arr = [1, 2, 3, 4]
    print(solve(arr))

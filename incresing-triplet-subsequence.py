def solve(nums):
    """
    Checks if an increasing triplet subsequence exists in the given list of numbers.

    Args:
        nums: A list of integers.

    Returns:
        True if an increasing triplet subsequence exists, False otherwise.
    """
    if len(nums) < 3:
        return False

    first = float("inf")
    second = float("inf")

    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True  # Found an increasing triplet

    return False


if __name__ == "__main__":
    nums = [20, 100, 10, 12, 5, 13]
    # print result of increasing triplet subsequence
    print(solve(nums))

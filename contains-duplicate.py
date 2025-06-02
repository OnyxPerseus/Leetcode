def solve(nums):
    """
    Determines if the input array contains any duplicate elements.
    
    Args:
        nums: List of integers
        
    Returns:
        True if the array contains duplicates, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Optimization for very small arrays
    if len(nums) <= 1:
        return False
    
    # For arrays with just 2 elements, direct comparison is faster
    if len(nums) == 2:
        return nums[0] == nums[1]
    
    # Use a set to track seen elements
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__ == '__main__':
    nums = [1,2,3,1]
    print(solve(nums))

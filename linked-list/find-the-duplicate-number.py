# use negative mark technique
def solve(nums):
    for num in nums:
        idx = abs(num)
        if nums[idx] < 0:
            return idx
        nums[idx] *= -1
    return -1

if __name__ == '__main__':
    nums = [1,3,4,2,2]
    print(solve(nums))
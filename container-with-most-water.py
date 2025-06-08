def solve(height):
    res = 0
    l, r = 0, len(height) - 1
    while l < r:
        y = min(height[l], height[r])
        res = max(res,y * (r - l))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return res


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solve(height))

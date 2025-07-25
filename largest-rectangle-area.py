def solve(heights):
    n = len(heights)
    maxArea = 0
    stack = []

    for i in range(n + 1):
        while stack and (i == n or heights[stack[-1]] >= heights[i]):
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        stack.append(i)
    return maxArea


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    print(solve(heights))

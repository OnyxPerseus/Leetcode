def solve(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    l, r = 0, n * m - 1
    while l <= r:
        mid = (l + r) // 2
        row = mid // m
        col = mid % m
        if target < matrix[row][col]:
            r = mid - 1
        elif target > matrix[row][col]:
            l = mid + 1
        else:
            return True
    return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(solve(matrix, target))

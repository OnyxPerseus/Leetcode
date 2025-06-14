def solve(temperatures):
    res = [0] * len(temperatures)
    stack = []  # stack position of the before days

    for index, today in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < today:
            i = stack.pop()
            res[i] = index - i
        stack.append(index)
    return res


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solve(temperatures))

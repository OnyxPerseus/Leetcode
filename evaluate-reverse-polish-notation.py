def solve(tokens):
    stack = []

    for x in tokens:
        if x == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif x == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif x == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif x == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a / b))
        else:
            stack.append(int(x))
    return stack.pop()


if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    print(solve(tokens))

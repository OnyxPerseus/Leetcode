def solve(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c not in mapping:
            stack.append(c)
        elif not stack:
            return False
        elif len(stack) and mapping[c] != stack.pop():
            return False
    return len(stack) == 0


if __name__ == "__main__":
    s = "(]"
    print(solve(s))

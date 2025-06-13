def solve(n):
    res = []

    def backtrack(openN,closeN,parenthese):
        if n == openN == closeN:
            res.append(parenthese)
            return
        if openN < n:
            backtrack(openN+1,closeN,parenthese + '(')
        if openN > closeN:
            backtrack(openN,closeN + 1, parenthese + ')')
    backtrack(0,0,'')
    return res

if __name__ == '__main__':
    print(solve(3))

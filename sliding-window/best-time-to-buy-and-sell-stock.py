def solve(prices):
    res = 0
    b = prices[0]
    for price in prices:
        res = max(res, price - b)
        b = min(b, price)
    return res


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    print(solve(prices))

def solve(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)
    res = 0
    prevTime = 0

    for p, s in cars:
        t = (target - p) / s
        if prevTime < t:
            res += 1
            prevTime = t
    return res


if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(solve(target, position, speed))

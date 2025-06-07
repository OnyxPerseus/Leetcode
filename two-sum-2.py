def solve(numbers,target):
    l,r = 0, len(numbers) - 1
    while l<r:
        s = numbers[l] + numbers[r]
        if s > target:
            r-=1
        elif s < target:
            l+=1
        else:
            return [l+1,r+1]

if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    print(solve(numbers,target))

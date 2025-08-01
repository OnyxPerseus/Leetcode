def solve(s1, s2):
    m = len(s1)
    n = len(s2)
    if m > n:
        return False

    countA = [0] * 26
    countB = [0] * 26
    l = 0
    match = 0  # variable save count match between two arrays

    for i in range(m):
        countA[ord(s1[i]) - ord("a")] += 1
        countB[ord(s2[i]) - ord("a")] += 1

    for i in range(26):
        match += (1 if countA[i] == countB[i] else 0)

    for i in range(m, n):
        if match == 26:
            return True

        inCharIdx = ord(s2[i]) - ord("a")
        countB[inCharIdx] += 1
        if countA[inCharIdx] == countB[inCharIdx]:
            match += 1  # if two count is equal
        elif countA[inCharIdx] + 1 == countB[inCharIdx]:
            match -= 1  # remove prev match

        outCharIdx = ord(s2[l]) - ord("a")
        countB[outCharIdx] -= 1
        if countA[outCharIdx] == countB[outCharIdx]:
            match += 1
        elif countA[outCharIdx] - 1 == countB[outCharIdx]:
            match -= 1
        l += 1

    return match == 26


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(solve(s1, s2))  # Output: True

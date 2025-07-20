def solve(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)
    l, r = 0, m - 1
    half = (m + n) // 2

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = nums1[i] if i >= 0 else float("-inf")
        Aright = nums1[i + 1] if (i + 1) < m else float("inf")
        Bleft = nums2[j] if j >= 0 else float("-inf")
        Bright = nums2[j + 1] if (j + 1) < n else float("inf")

        if Aleft <= Bright and Bleft <= Aright:
            if (m + n) % 2 != 0:
                return float(min(Aright, Bright))
            return float((max(Aleft, Bleft) + min(Aright, Bright))) / 2
        else:
            if Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print(solve(nums1, nums2))

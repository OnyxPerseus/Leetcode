from collections import defaultdict


class TimeMap:
    def __init__(self) -> None:
        self.map = defaultdict(list)

    def set(self, key, value, timestamp):
        self.map[key].append((value, timestamp))

    def get(self, key, timestamp):
        res = ""
        values = self.map[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                res = values[m][0]
                break
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                res = values[m][0]
                l = m + 1
        return res

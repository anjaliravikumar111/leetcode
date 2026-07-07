from collections import defaultdict
from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length):
        self.s = 0
        self.d = defaultdict(list)

    def set(self, i,v):
        self.d[i].append((self.s, v))

    def snap(self):
        self.s += 1
        return self.s - 1

    def get(self, i,s):
        a = self.d[i]
        j = bisect_right(a, (s, 10**9)) - 1
        return a[j][1] if j >= 0 else 0
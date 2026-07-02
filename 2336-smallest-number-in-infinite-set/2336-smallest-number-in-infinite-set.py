import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.heap = []
        self.seen = set()

    def popSmallest(self):

        if self.heap:
            val = heapq.heappop(self.heap)
            self.seen.remove(val)
            return val

        self.curr += 1
        return self.curr - 1

    def addBack(self, num):

        if num < self.curr and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)
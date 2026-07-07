class Solution:
    def findRightInterval(self, intervals):
        starts = sorted((x[0], i) for i, x in enumerate(intervals))
        ans = []
        for _, e in intervals:
            i = bisect_left(starts, (e,))
            ans.append(starts[i][1] if i < len(starts) else -1)
        return ans
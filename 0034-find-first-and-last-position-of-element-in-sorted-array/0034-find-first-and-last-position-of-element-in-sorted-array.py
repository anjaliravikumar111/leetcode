class Solution:
    def searchRange(self, nums, target):
        from bisect import bisect_left, bisect_right
        l = bisect_left(nums, target)
        r = bisect_right(nums, target) - 1
        return [l, r] if l <= r and l < len(nums) and nums[l] == target else [-1, -1]
class Solution:
    def maxOperations(self, nums, k):
        count = {}
        ans = 0

        for num in nums:
            target = k - num

            if count.get(target, 0) > 0:
                ans += 1
                count[target] -= 1
            else:
                count[num] = count.get(num, 0) + 1

        return ans
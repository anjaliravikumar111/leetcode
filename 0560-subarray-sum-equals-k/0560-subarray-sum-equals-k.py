from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            count += prefix_count[current_sum - k]

            prefix_count[current_sum] += 1

        return count
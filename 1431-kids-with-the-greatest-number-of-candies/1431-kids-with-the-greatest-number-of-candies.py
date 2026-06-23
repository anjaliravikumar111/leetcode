class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        
        res = []
        
        for i in candies:
            res.append(i + extraCandies >= maximum)
        
        return res
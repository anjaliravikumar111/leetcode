class Solution:
    def minFlips(self, a,b,c):
        flips = 0
        for i in range(31):
            
            if (c >> i) & 1:
                flips += ((a >> i) & 1) == 0 and ((b >> i) & 1) == 0
            
            else:
                flips += (a >> i) & 1
                flips += (b >> i) & 1
        return flips
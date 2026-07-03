class Solution:
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        Tribonacci = [0] * (n + 1)
        Tribonacci[0] = 0
        Tribonacci[1] = 1
        Tribonacci[2] = 1
        for i in range(3, n + 1):
            Tribonacci[i] = Tribonacci[i-1] + Tribonacci[i-2] + Tribonacci[i-3]
        return Tribonacci[n]
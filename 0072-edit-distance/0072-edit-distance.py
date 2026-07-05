class Solution:
    def minDistance(self, word1,word2):
        m = len(word1)
        n = len(word2)
        dp = [i for i in range(m, -1, -1)]

        for i2 in range(n - 1, -1, -1):
            ndp = [0] * (m + 1)
            ndp[-1] = n - i2
            for i1 in range(m - 1, -1, -1):
                if word1[i1] == word2[i2]:
                    ndp[i1] = dp[i1 + 1]
                    continue
                insert = dp[i1]
                delete = ndp[i1 + 1]
                replace = dp[i1 + 1]
                ndp[i1] = 1 + min(insert, delete, replace)
            dp = ndp

        return dp[0]
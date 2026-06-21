from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):

        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:n1])

        if s1_count == window_count:
            return True

        for i in range(n1, n2):

            window_count[s2[i]] += 1
            window_count[s2[i - n1]] -= 1

            if window_count[s2[i - n1]] == 0:
                del window_count[s2[i - n1]]

            if window_count == s1_count:
                return True

        return False
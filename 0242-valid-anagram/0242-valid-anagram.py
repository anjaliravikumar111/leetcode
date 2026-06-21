class Solution(object):
    def isAnagram(self, s, t):

        if len(t) != len(s):
            return False

        return sorted(t) == sorted(s)
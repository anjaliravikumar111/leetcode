class Solution(object):
    def reverseWords(self, s):
        # Python 2 equivalent
        words = s.split()
        return " ".join(reversed(words))
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        
        n = self.gcd(len(str1), len(str2))
        return str1[:n]
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
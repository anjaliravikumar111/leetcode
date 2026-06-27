from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        radiant = deque()
        dire = deque()
        n = len(senate)
        
        for i, char in enumerate(senate):
            if char == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
                
        return "Radiant" if radiant else "Dire"
from collections import Counter

class Solution:
    def equalPairs(self, grid):
        row_counts = Counter(tuple(row) for row in grid)
        
        pair_count = 0
        n = len(grid)
        
        for col_idx in range(n):
            col = tuple(grid[row_idx][col_idx] for row_idx in range(n))
            pair_count += row_counts[col]
            
        return pair_count
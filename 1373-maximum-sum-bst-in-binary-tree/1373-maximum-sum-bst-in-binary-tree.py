class Solution:
    def maxSumBST(self, root):
        self.ans = 0
        def solve(node):
            if not node:
                return 0, float('inf'), float('-inf'), True
            
            l_sum, l_min, l_max, l_bst = solve(node.left)
            r_sum, r_min, r_max, r_bst = solve(node.right)
            
            if l_bst and r_bst and l_max < node.val < r_min:
                current_sum = node.val + l_sum + r_sum
                self.ans = max(self.ans, current_sum)
                return current_sum, min(l_min, node.val), max(r_max, node.val), True
            
            return 0, float('-inf'), float('inf'), False
            
        solve(root)
        return self.ans
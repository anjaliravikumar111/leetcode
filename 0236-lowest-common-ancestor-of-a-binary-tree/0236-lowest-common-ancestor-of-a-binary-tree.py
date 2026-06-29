class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Base case: if we hit a dead end, or find either target node
        if not root or root == p or root == q:
            return root
            
        # Look for p and q in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If left and right both returned something, it means p is on one side 
        # and q is on the other. This node is their lowest common meeting point!
        if left and right:
            return root
            
        # If only one side returned a node, pass that result up the tree
        return left if left else right
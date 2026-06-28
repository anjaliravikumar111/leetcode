 
class Solution:
    def leafSimilar(self, root1,root2):
        def helper(root,leaves):
            if root is None:
                return False
            if root.left is None and root.right is None:
                leaves.append(root.val)
            helper(root.left,leaves)
            helper(root.right,leaves)
            return leaves
        return helper(root1,[]) == helper(root2,[])
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Node with only one child or no child
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            # Node with two children:
            # Get the inorder successor (smallest in right subtree)
            temp = root.right
            while temp.left:
                temp = temp.left

            # Copy inorder successor's value to this node
            root.val = temp.val

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)

        return root
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            min_right = root.right
            while min_right.left:
                min_right = min_right.left
            root.val = min_right.val
            root.right = self.deleteNode(root.right, root.val)

        return root

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root!=None:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        else:
            return[]

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root!=None:
            return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
        else:
            return[]

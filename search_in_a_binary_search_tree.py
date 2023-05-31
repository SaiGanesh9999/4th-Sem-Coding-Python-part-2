class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ptr=root
        while(ptr!=None):
            if ptr.val==val:
                return ptr
            elif val<ptr.val:
                ptr=ptr.left
            else:
                ptr=ptr.right 
        return None

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        res = None
        
        def dfs(node):
            nonlocal cnt, res
            
            if not node or res is not None:
                return
            
            dfs(node.left)
            cnt += 1
            if cnt == k:
                res = node.val
                return
            
            dfs(node.right)
            
        dfs(root)
        return res
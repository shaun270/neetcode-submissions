class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # If the helper returns -1, it's unbalanced. Otherwise, it's balanced.
        return self.checkHeight(root) != -1
        
    def checkHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        # 1. Check the left side from below
        left = self.checkHeight(root.left)
        if left == -1: return -1 # Imbalance found deeply, pass the error up
        
        # 2. Check the right side from below
        right = self.checkHeight(root.right)
        if right == -1: return -1 # Imbalance found deeply, pass the error up
        
        # 3. Now check THIS node's balance
        if abs(left - right) > 1:
            return -1 # This node is unbalanced, trigger the error
            
        # 4. If everything is fine, return the actual height
        return 1 + max(left, right)
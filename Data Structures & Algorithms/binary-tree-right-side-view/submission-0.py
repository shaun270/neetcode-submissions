# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 1 -> 2, 3
        # [2,3] -> [4, 5]

        from collections import deque
        queue = deque([root])
        if not root:
            return []
        output = [root.val]
        while queue:
            level = []
            for i in range(len(queue)):
                ele = queue.popleft()
                if ele.left:
                    level.append(ele.left)
                    queue.append(ele.left)
                if ele.right:
                    level.append(ele.right)
                    queue.append(ele.right)
            if len(level) != 0:
                output.append(level[-1].val)
        
        return output
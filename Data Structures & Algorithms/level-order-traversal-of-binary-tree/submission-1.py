# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        final_list = []
        q = deque()
        curr = root
        q.append(curr)
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            if level:
                final_list.append(level)
        
        return final_list
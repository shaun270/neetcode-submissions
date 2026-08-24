# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []

        final_result = []
        q = deque()
        q.append(root)

        while q:
            total_length = len(q)
            for i in range(total_length):
                ele = q.popleft()
                if i == total_length - 1:
                    final_result.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)

        return final_result

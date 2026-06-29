# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node, p, q):
            if p.val <= node.val and node.val <= q.val:
                return node
            elif node.val > p.val and node.val > q.val:
                return dfs(node.left, p, q)
            else:
                return dfs(node.right, p, q)
        p, q = (p, q) if p.val <= q.val else (q, p)
        return dfs(root, p, q)
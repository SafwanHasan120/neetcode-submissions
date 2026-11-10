# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        def dfs(root, maxSoFar):
            nonlocal res
            if not root:
                return None
            if root.val >= maxSoFar:
                res += 1
            dfs(root.left, max(maxSoFar, root.val))
            dfs(root.right, max(maxSoFar, root.val))
        dfs(root, -101)
        return res
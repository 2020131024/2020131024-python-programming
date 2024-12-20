# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        while root:
            if p.val <= root.val <= q.val:
                return root
            else:
                if p.val < root.val and q.val < root.val:
                    root = root.left
                else:
                    root = root.right
                    
        return root

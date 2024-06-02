# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def checkSymmetric(node_1, node_2):
            val_1 = node_1.val if node_1 else None
            val_2 = node_2.val if node_2 else None

            if val_1 is None and val_2 is None:
                return True
            elif val_1 != val_2:
                return False
            
            return checkSymmetric(node_1.left, node_2.right) and checkSymmetric(node_1.right, node_2.left)
        
        return checkSymmetric(root.left, root.right)

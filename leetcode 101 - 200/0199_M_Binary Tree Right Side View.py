# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            result.append(queue[-1].val)

            next_queue = []
            for node in queue:

                if node.left:
                    next_queue.append(node.left)

                if node.right:
                    next_queue.append(node.right)

            queue = None if len(next_queue) == 0 else next_queue
        
        return result
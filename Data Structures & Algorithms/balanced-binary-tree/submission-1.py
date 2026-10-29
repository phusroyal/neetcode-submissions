# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def node_height(root):
            if root is None:
                return 0
            
            left = node_height(root.left)
            right = node_height(root.right)
        
            return 1 + max(left, right)

        left_height = node_height(root.left)
        right_height = node_height(root.right)

        return (
            abs(left_height - right_height) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )


            
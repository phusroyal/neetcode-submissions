# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.preorder_traversal(p) == self.preorder_traversal(q)

    
    def preorder_traversal(self, root:Optional[TreeNode]) -> list:
        result = []

        def dfs(node):
            if node is None:
                result.append('null')
                return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return result

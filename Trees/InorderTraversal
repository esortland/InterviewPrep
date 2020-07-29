# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.trav(root, res)
        return res
        
    def trav(self, root, res):
        if root.left:
            self.trav(root.left, res)
        res.append(root.val)
        if root.right:
            self.trav(root.right, res)

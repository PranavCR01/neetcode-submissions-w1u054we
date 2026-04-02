# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        max_so_far = 0
        
        def good(node, max_so_far):
            nonlocal count 
            if not node:
                return 0
            
            if node.val >= max_so_far:
                count += 1
            
            max_so_far = max(node.val, max_so_far)
        
            good(node.left, max_so_far)
            good(node.right, max_so_far)
        good(root, float('-inf'))
        return count






























        
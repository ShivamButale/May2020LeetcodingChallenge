# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#nbNB
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        x = 0
        z = []
        z = self.inorder(root, k, z)
        return z[k-1]
        
    def inorder(self,root, k, z):
        if root.left:
            self.inorder(root.left, k, z)
        
        z.append(root.val)
        
        if root.right:
            self.inorder(root.right, k, z)
            
        return z

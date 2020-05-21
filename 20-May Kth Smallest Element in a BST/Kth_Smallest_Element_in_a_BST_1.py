# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Inorder(self, root):
        if root is None:
            return []
        return self.Inorder(root.left) + [root.val] + self.Inorder(root.right)
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #Inorder traveersal  gives us elements in ascendi order. then just find kth element present at index k-1
        return  self.Inorder(root)[k-1]    

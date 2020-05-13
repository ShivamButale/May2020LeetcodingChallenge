# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #We will do level order traversal (LOT). If x and y are at same level and have distinct parents, they are cousins
        #Initialize stack with root 
        stack = [root]

        #Need to Check whether x or y are present in current level
        while stack:    
            pr1=0  #Variable to indicate x is present
            pr2=0  #Variable to indicate y is present
            #Check for current level if x and y are present in it
            for elem in stack:
                if elem.val==x:
                    pr1 = 1 
                if elem.val==y:
                    pr2 = 1
            #If both are found, they are at same level in LOT and are cousins Return True
            if pr1==1 and pr2==1:
                return True
            #If only one of them was detected, the are not at same level, hence not cousins, Return False
            if pr1==1 or pr2==1:
                return False
            
            #Both not found.Now update stack with children of elements present in current stack
            
            #Prepare stack for new level
            new_stack = []            
            #If they have same parents, return False
            for i in stack:
                #If children of curr element equal to x and y, same parents, return False
                if i and i.left and i.right and ((i.left.val==x and i.right.val==y) or (i.right.val==x and i.left.val==y)):
                    return False 
                if i.left:
                    new_stack.append(i.left)
                if i.right:
                    new_stack.append(i.right)
            
            #Intialize stack to new stack
            stack = new_stack
        #If True was not returned after all traversals are over, return False
        return False

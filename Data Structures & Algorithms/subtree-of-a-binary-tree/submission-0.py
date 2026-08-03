# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #I will call the helper fuction on the two nodes with the same val
        if not subRoot:
            return True
        if not root:
            return False
        
        #i will pass it in to the sameTree helper
        if self.sameTree(root, subRoot):
            return True

        #now if they exisits call the helper on them and if one return the we are good
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        #if one returns true then it is true
        return left or right
 
    #set up the helper
    def sameTree(self, r, s):
        if not r and not s:
            return True
        if not r or not s:
            return False
        if r.val != s.val:
            return False
        
        left = self.sameTree(r.left, s.left)
        right = self.sameTree(r.right, s.right)

        return left and right | False



    '''
    U - I can create a helper function, that will check of the tree at a given node 
        is the same or not. 

        To do this i need to check if the two nodes are none then that is true
        if one node is true and anotehr is false then return false
        if val of node is true then keep going recursivley.

        Once i do that in the main subtree i need to check a few things 
        if root exists and subroot does not that is could be true
        if root does not exists and subroot does that is could be False
        if root and subroot are not the same val false
    ''' 

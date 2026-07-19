# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base cases
        # if p none and q none -> True check first to avoid a false flase
        if not p and not q:
            return True
        # if p none or q are none -> return False
        if not p or not q:
            return False
        # if p.val != q.val -> False
        if p.val != q.val:
            return False
        #recursive equation
        #build the left 
        left  = self.isSameTree(p.left, q.left)
        #build the right
        right = self.isSameTree(p.right, q.right)
        # If only true true return true else False
        if left and right:
            return True
        else:
            return False
        # F F -> f
        # F T -> F
        # T F -> F
        # T T -> T

        '''
        What should the recursive function return?
        True or False?
        What information does the parent need from the children?
        check if node.left , node.right == node.right, node.left that will be True or False
        What is the base case? 
        The base is if not node return None
        Why is it preorder, inorder, or postorder?
        We don't need the children to finish if they are the same or not for parent 
        we can go ahead and comapre each child from root
        '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right | False
        


        '''
        U - Given two binary trees i am expected to check if they are the same or not
            So i can try to break this probelm down to simple checks. 
            One for two nodes to be the same if we keep going down recursively and 
            reach a leaf node. the value of the nodes will be none / if p and q are
            both none then that is true, if they have diff vals then that is false
            or if one is none and the other is not then that is false

            after that we can call recusrivly on left and right and do logic check 
            if left | R
                T       T = T
                F       T = F
                F       F = F
                T       F = F
        '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def getHeight(node):
            nonlocal isBalanced
            #base case
            if not node:
                return 0
            
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)

            #Now that i have both height i can check for imlance
            if abs(leftHeight - rightHeight) > 1:
                isBalanced = False

            return max(leftHeight, rightHeight) + 1
        #call get height on root
        getHeight(root)
        return isBalanced

        '''
        Given a binary tree, i need to check if the height is balanced. 
        Height that is balanced is at any node in the tree the left and right subtress 
        can not differ by no more than 1

        I am thinking of checking at each node using DFS if the subtrees for that node 
        are balanced if so then we will keep our global Var True 
        if leftHeight - rightHeight > 1 or rightHeight - leftHeight > 1 then False

        Our DFS or recursive function should return the depth of the subtree
        '''   
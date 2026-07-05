# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case
        if not root:
            return None
        #logic to invert
        root.right, root.left = root.left, root.right
        #Now we call function on both left and right
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


    '''
        Given the root of a binary tree i am asked to go ahead and invert the children
        of each node the rigth to the left and the left to the right and finally return
        the root node

        Now My brain is thinking of using recursion to solve this in subproblems and build 
        my final answer

        What should the recursive function return?
            It should return Node ( root ) of the inverted subtree
        What information does the parent need from the children? 
            I need the node of the
        What is the base case?
            If not node return None
        Why is it preorder, inorder, or postorder?
            I am thinking preOrder becuase the curr node doesn't need the children to 
            finsih processing for the recursion to work
    ''' 
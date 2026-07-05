# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case
        if not root:
            return 0
        #if node exists 
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        #once we get both depth from subtree then we take the max and add one
        return max(leftDepth, rightDepth) + 1


        '''
        U - given a root of a binary tree i am asked to return the depth. I am thinking of a recursive 
            approach by asking each node what its subtrees depth is and keep returning that to the top
            then i will comapre whether the left or right has more depth and finally return the maxdepth
        M - I will be using DFS, Post-order Treversal becuase i need the answer from the left subtree and 
            right subtree before returning my final call (root) left -> right -> root is post
        P - I will have a baseCase where is node is null then return 0 becuase that means there is no node
            to take into account
            I will call leftdpeth on the left child 
            and rightDepth on the right child 

            when i return i need to compare which on is more lengthy / max and add one to account for curr node
        '''
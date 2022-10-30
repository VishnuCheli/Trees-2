#Time Complexity:: O(n)-all nodes are visited in each level
#Space Complexity:: O(1)-a current sum is added to a result variable.
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0 #result is initialized with 0
        self.inOrder(root,0) #initialy current sum is set to 0
        return self.result 
    
    def inOrder(self,root,currSum):
        #base
        if root == None:
            return
        
        #logic
        self.inOrder(root.left,currSum*10+root.val) #every node visited has it's current sum calculated
        
        self.inOrder(root.right,currSum*10+root.val) 
        
        #leaf node check
        if root.left == None and root.right==None: #check left and right child is null for lead node
            self.result += currSum*10 + root.val #when the leaf node is touched the currsum of that path is added to the result
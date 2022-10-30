#Time Complexity:: O(n)-all nodes are visited
#Space Complexity:: O(n*p)-a path list is used where p is number of paths
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.target = targetSum #initializing targetsum as a global variable
        self.result = [] #creating a global list of paths
        self.recur(root,0,[]) #initially passing current sum as 0 and empty path list 
        return self.result
    
    def recur(self, root, currSum, path):
        #base
        if root == None:
            return 
        
        #current sum calculation
        currSum = currSum + root.val #new current sum calculated
        path.append(root.val) #each nodes value is appended to path
        
        #logic
        self.recur(root.left,currSum,path)
        
        if root.left == None and root.right == None: #check for leaf node
            if currSum == self.target:
                temp = path[:] #shallow copy all node values from path to a temp list alternative( copy.path)
                #data structure inside data structure is a pointer, paths in the recursive stack, the path list is just a pointer to the previous path, therefore we pop the path.
                #In that case instead popping all path in temp variable and append, then pop path
                self.result.append(temp) 
        
        self.recur(root.right,currSum,path)
        
        #backtracking
        path.pop() #everytime you go back to a parent node, pop the already traversed path
            
        
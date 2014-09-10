# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    accum = 0
    def firTravel(self,root,sum):
        self.accum += root.val
        print self.accum
        if self.accum == sum and root.left == None and root.right == None:
            return True
        if root.left:
            if self.firTravel(root.left,sum):
                return True
        if root.right:
            if self.firTravel(root.right,sum):
                return True
        self.accum -= root.val
        return False
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self,root,sum):
        if root == None:
        	return False
        return self.firTravel(root,sum)
if __name__ == '__main__':
    Slu = Solution()
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    a.left = b
    a.right = c
    print Slu.hasPathSum(a,6)


        

        

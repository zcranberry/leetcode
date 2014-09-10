# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

INT_MIN = - 2 ** 32
class Solution:
    # @param root, a tree node
    # @return a boolean
    def inOrder(self,root):
        if root.left != None:
            if self.inOrder(root.left) == False:
                return False
        self.prev = self.curr
        self.curr = root.val
        #print 'prev:' + str(self.prev)
        #print 'curr:' + str(self.curr)
        if self.curr <= self.prev:
            return False
        if root.right != None:
            if self.inOrder(root.right) == False:
                return False

    def isValidBST(self, root):
        if root == None:
            return True
        self.prev = INT_MIN
        self.curr = INT_MIN + 1
        if self.inOrder(root) == False:
            return False
        else:
            return True

if __name__ == '__main__':
    node1 = TreeNode(1) 
    node3 = TreeNode(1) 
    node2 = TreeNode(1, node1) 
    slu = Solution()
    print slu.isValidBST(node2)

                


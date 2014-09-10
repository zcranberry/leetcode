class TreeNode:
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r
class Solution:
    # @param root, a tree node
    # @return a list of integers
    res = []
    def in_travel(self, root):
        if root.left:
            self.in_travel(root.left)
        self.res.append(root.val)
        if root.right:
            self.in_travel(root.right)
    def inorderTraversal(self, root):
        del self.res[:]
        if root != None:
        	self.in_travel(root)
        return self.res

if __name__ == '__main__':
    node1 = TreeNode(1) 
    node3 = TreeNode(3) 
    node2 = TreeNode(2, node1, node3) 
    slu = Solution()
    print slu.inorderTraversal(node2)
    print node2.left

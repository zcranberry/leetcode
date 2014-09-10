from TreeNode import TreeNode, rebuildBinary
class Solution:
    # @param root, a tree node
    # @return an integer
    summ = 0
    curr = 0
    def preOrder(self, root):
        self.curr = self.curr * 10 + root.val
        if root.left == None and root.right == None:
        	self.summ += self.curr
        if root.left:
        	self.preOrder(root.left)
        if root.right:
        	self.preOrder(root.right)
        self.curr /= 10

    def sumNumbers(self, root):
        self.summ = 0
        self.curr = 0
        if root != None:
            self.preOrder(root)
        return self.summ

if __name__ == '__main__':
	root = rebuildBinary([1,2,3])
	slu = Solution();
	print slu.sumNumbers(root)


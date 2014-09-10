#encoding:UTF-8
from TreeNode import *
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def __flatten(self, root):
        if root.left:
            self.__flatten(root.left)
        if root.right:
            self.__flatten(root.right)
        if root.left:#找到左子树中最后一个
            curr = root.left
            while curr.right != None:
                curr = curr.right
            curr.right = root.right #右子树挂到该节点下
            root.right = root.left 
            root.left = None
    def flatten(self, root):
        if root:
        	self.__flatten(root)

if __name__ == '__main__':
    slu = Solution()
    root = rebuildBinary(range(1,8))
    print 'pre'
    preOrder(root)
    print 'in'
    inOrder(root)
    print 'post'
    postOrder(root)
    slu.flatten(root)
    print 'pre'
    preOrder(root)
    print 'in'
    inOrder(root)
    print 'post'
    postOrder(root)





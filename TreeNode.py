#encoding:UTF-8
#解决leetcode上链表的输入问题
from collections import deque
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def rebuildBinary(in_list):#输入in_list形入[1,#,2],为一个list
    root = TreeNode(in_list[0])
    queue = deque()
    queue.append(root)
    length = len(in_list) / 2 #给节点指定左子树和右子树的次数
    for i in xrange(0, length):
        curr = queue.popleft()
        if in_list[2 * i + 1] != '#':
            curr.left  = TreeNode(in_list[2 * i + 1])
            queue.append(curr.left)
        if in_list[2 * i + 2] != '#':
            curr.right = TreeNode(in_list[2 * i + 2])
            queue.append(curr.right)
    if length % 2 == 0:#处理最后只有左节点的情况
    	curr = queue.popleft()
        if in_list[-1] != '#':
        	curr.left = TreeNode(in_list[-1])

    return root

def preOrder(root):
    print root.val
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)

def inOrder(root):
    if root.left:
        inOrder(root.left)
    print root.val
    if root.right:
        inOrder(root.right)

def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print root.val

if __name__ =='__main__':
    root = rebuildBinary([1,2,3])
    print 'pre'
    preOrder(root)
    print 'in'
    inOrder(root)
    print 'post'
    postOrder(root)

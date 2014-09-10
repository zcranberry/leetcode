# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

def isSymm(p,q):
    if p != None and q != None:
    	return p.val == q.val and isSymm(p.left,q.right) and isSymm(p.right,q.left)
    elif p != None or q != None:
        return False
    else:
    	return True
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
        	return True
        return isSymm(root.left,root.right)

if __name__ == '__main__':
	node2 = TreeNode(2)
	node3 = TreeNode(2)
	node1 = TreeNode(1, node2, node3)
	slu = Solution()
	print slu.isSymmetric(node1)

        

#http://oj.leetcode.com/problems/same-tree/
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p != None and q != None:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        elif p != None or q != None:
            return False
        else:
            return True

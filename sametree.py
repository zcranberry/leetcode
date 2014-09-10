#这道题用如下的方式不对，有同样的val的节点时不可以
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def fir_order(root,res_list):
    if root != None:
        res_list.append(root.val)
        fir_order(root.left, res_list)
        fir_order(root.right, res_list)
    else:
        return

def mid_order(root,res_list):
    if root != None:
        mid_order(root.left, res_list)
        res_list.append(root.val)
        mid_order(root.right, res_list)
    else:
        return

#fir_order(node1)
#mid_order(node1)
#for each in fir_res_list:
#    print each
#for each in mid_res_list:
#    print each


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolea`n

    def isSameTree(self, p, q):
        lenp = -1
        lenq = -1
        try:
            if len(p) == 0:
            	lenp = 0
        except:
            pass
        try:
            if len(q) == 0:
            	lenq = 0
        except:
            pass
        
        if lenp == 0 or lenq == 0:
            if lenp ==0 and lenq == 0:
            	return True
            else:
            	return False
                
        p_fir = []
        p_mid = []
        q_fir = []
        q_mid = []
        fir_order(p, p_fir)
        mid_order(p, p_mid)
        fir_order(q, q_fir)
        mid_order(q, q_mid)
        if p_fir == q_fir and p_mid == q_mid:
            return True
        else:
            return False

if __name__ == '__main__':
    slu = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    a = {}
    b = {}
    print(slu.isSameTree(node1, node1))


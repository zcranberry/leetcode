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
if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    rest_list = []
    fir_order(node1,rest_list)
    for each in rest_list:
    	print each


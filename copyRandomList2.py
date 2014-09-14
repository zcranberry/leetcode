#encoding:UTF-8
#应考虑用继承使ListNode特性更丰富
from myList import *
from random import randint
# Definition for singly-linked list with a random pointer.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         self.random = None
#g_copiedArray = []
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def copyRandomList(self, head):
        pos_hash = {}
        nodeArray = []
        count = 0
        if head == None:
            return
        copyHead = RandomListNode(head.label)
        curr = head
        curr2 = copyHead
        next = curr.next
        pos_hash[curr] = count
        nodeArray.append(curr2)

        while(next):
            curr = next
            next = curr.next
            count += 1
            newNode = RandomListNode(curr.label)
            curr2.next = newNode
            curr2 = newNode
            pos_hash[curr] = count
            nodeArray.append(curr2)
        
        curr = head
        curr2 = copyHead
        while(curr):
            if (curr.random): #may be None
                pos = pos_hash[curr.random]
                curr2.random = nodeArray[pos]
            curr = curr.next
            curr2 = curr2.next

        #global g_copiedArray 
        #g_copiedArray = nodeArray
        return copyHead

if __name__ == '__main__':
    array = range(1, 8)
    NodeHead = buildList(range(1, 8))
    for i in range(0 ,len(array)):
        NodeArray[i].random = NodeArray[randint(0, 6)]
    copiedHead = Solution().copyRandomList(NodeHead)
    print 'oriList'
    travelByHead(NodeHead)
    print 'copiedList'
    travelByHead(copiedHead)
    print 'ByArray'
    travelByArray(NodeArray)


    print 'oriRandom'
    for each in NodeArray:
        print '%s random points to %s ' % (each.pos, each.random.pos)

    print 'copiedRandom'
    for each in g_copiedArray:
        print '%s random points to %s ' % (each.pos, each.random.pos)


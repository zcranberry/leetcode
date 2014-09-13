from myList import *
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None:
            return 
        count = 0
        ori_head = head
        while(head):
            #print head.val
            head = head.next
            count += 1
        half_count = (count + 1) / 2

        #print 'total_count %s' % half_count


        head = ori_head
        while(half_count > 1):
        #    print head.val
            head = head.next
            half_count -= 1

        sec_head = head.next
        head.next = None

        #print 'first part'
        #travelByHead(ori_head)

        reversed_head = reverse_List(sec_head)

        #print 'second part'
        #travelByHead(reversed_head)
        
        merge(ori_head, reversed_head)
        #print 'after merge'
        #travelByHead(ori_head)

def merge(head1, head2):
    ori_head = head1
    while(head1 and head2):
        next_head1 = head1.next
        next_head2 = head2.next
        head1.next = head2
        head2.next = next_head1
        head1 = next_head1
        head2 = next_head2

def reverse_List(head, tail = None):
    if head == tail or head.next == tail:
        return head
    curr = tail
    nextN = head
    while nextN != tail:
        nextnext = nextN.next
        nextN.next = curr
        curr = nextN
        nextN = nextnext
    #global NodeHead
    #NodeHead = curr
    return curr


if __name__ == '__main__':
    NodeHead = buildList([1,2,3,4])
    Solution().reorderList(NodeHead)

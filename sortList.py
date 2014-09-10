#encoding:UTF-8
#用到了三向切分，可以过AC快排，但是过不了插入排序，不知道怎么shuffle
from myList import *
from time import clock
import random
def sortList_quick(head, tail):
    if head is tail:
        return
    prev = head
    if prev.next == tail or prev.next.next == tail:#0-1 Node
        return
    else:
        curr = prev.next

    pivot = curr.val
    pivot_pos = curr
    prev = curr
    curr = curr.next
    while curr != tail:
        if curr.val < pivot:
            prev.next = curr.next
            curr.next = head.next
            head.next = curr
            curr = prev.next
        elif curr.val == pivot_pos:
            if pivot.next == curr:#without it will cause infinite loop
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr.next = pivot_pos.next
                pivot_pos.next = curr
                curr = prev.next
        else:
            prev = curr
            curr = curr.next
    pivot_last = pivot_pos
    while pivot_last.next != None and pivot_last.next.val == pivot:
    	pivot_last = pivot_last.next
    sortList_quick(head,pivot_pos)
    sortList_quick(pivot_last,tail)



class Solution():
    def sortList(self,head):
        before_head = ListNode(1000)
        before_head.next = head
        sortList_quick(before_head, None)
        return before_head.next

if __name__ == "__main__":
    ori_list = range(1,5000)
    random.shuffle(ori_list)
    alist = buildList(ori_list)
    #travel(alist)
    start = clock()
    res = Solution().sortList(alist)
    time_cons = clock() - start
    #travel(res)
    print time_cons



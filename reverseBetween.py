#encoding:UTF-8
from myList import *

def myReverseBetween(head,m,n):
    count = 0
    prev = ListNode(-1)
    prev.next = head
    cursor = head
    while count < m:
        cursor = cursor.next
        prev = prev.next
        count += 1
    mark1 = prev
    while count < n:
        cursor = cursor.next
        count += 1
    mark2 = cursor
    
    #print 'mark1',mark1.pos
    #print 'mark2',mark2.pos
    global NodeArray
    travelByArray(NodeArray)
    reverse_List(mark1.next, mark2.next)
    travelByArray(NodeArray)

    mark1.next = mark2
    if m != 0:
    	return head
    else:
    	return mark2

if __name__ == '__main__':
    head = buildList(range(0,6))
    head = myReverseBetween(head, 0, 4)
    travelByArray(NodeArray)
    travelByHead(head)

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        while(head):
            print head.val
            head = head.next


if __name__ == '__main__':
    Solution()

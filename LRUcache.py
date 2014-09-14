#encoding:UTF-8
class ListNode:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def delete(self, curr):#delte may happen in the list or the tail
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1
    
    def insert(self, curr):#before head
        curr.next = self.head.next
        curr.prev = self.head
        self.head.next.prev = curr
        self.head.next = curr
        self.size += 1

    # @return an integer
    def get(self, key):
        found = False
        curr = self.tail.prev
        while(curr!= self.head):
            if curr.key == key:
                found = True
                value = curr.value
                self.delete(curr)
            curr = curr.prev
        if found:
            newNode = ListNode(key, value)
            self.insert(newNode)
        return value if found else -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        found = False
        curr = self.tail.prev
        while(curr != self.head):
            if curr.key == key:# found
                found = True
                self.delete(curr)
            curr = curr.prev
        #insert after head
        newNode = ListNode(key, value)
        self.insert(newNode)

        if self.size > self.capacity:
            self.delete(self.tail.prev)


if __name__ == '__main__':
    cache = LRUCache(3)
    cache.set('one', 1)
    cache.set('two', 2)
    cache.set('three', 3)
    cache.set('four', 4)
    print cache.get('three')
    print cache.get('one')
    head = cache.head
    while(head):
        print head.key, head.value
        head = head.next


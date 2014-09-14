#encoding:UTF-8
class ListNode:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
        
    def __delete(self, curr):#delte may happen in the list or the tail
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1
    
    def __insert(self, curr):#before head
        curr.next = self.head.next
        curr.prev = self.head
        self.head.next.prev = curr
        self.head.next = curr
        self.size += 1

    def get(self, key):
        found = False
        if key in self.hashmap:
            found = True
            node = self.hashmap[key]
            value = node.value
            self.__delete(node)
            #newNode = ListNode(key, value)
            self.__insert(node)
            #self.hashmap[key] = newNode
            return value
        else:
            return -1
            
    def set(self, key, value):
        if key in self.hashmap:
            node = self.hashmap[key]
            self.__delete(node)
        newNode = ListNode(key, value)
        self.__insert(newNode)
        self.hashmap[key] = newNode
            
        if self.size > self.capacity:
            del self.hashmap[self.tail.prev.key]
            self.__delete(self.tail.prev)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.set('one', 1)
    cache.set('two', 2)
    cache.set('three', 3)
    cache.set('four', 4)


    #head = cache.head
    #while(head):
    #    print head.key, head.value
    #    head = head.next


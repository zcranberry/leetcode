#encoding:UTF-8
class ListNode:
    def __init__(self, pos, val = None , next = None):
        self.val = val
        self.pos = pos
        self.next = next

#按说应该封入一个类里面，这里放全局变量里
NodeCount = 0
NodeHead = None
NodeArray = []
#要在表头前面插入，需要封装下表头
def insertAfter(prev,Node):#how to deal with head
    Node.next = prev.next
    prev.next = Node
    NodeCount += 1

def insertBefore(Node):
    global NodeHead, NodeCount
    Node.next = NodeHead
    NodeHead = Node
    NodeCount += 1

def delNode(prev):
    prev.next = prev.next.next
    NodeCount -= 1

#给一个List,return一个head,改成全局head之后不return也行
def buildList(array): #这个目前从0开始才正确，不接受自定义的array
    global NodeArray
    global NodeHead
    length = len(array)
    if length == 0:
        return None
    for i in range(length - 1, -1, -1):
        newNode = ListNode(i, array[i])
        insertBefore(newNode)
        NodeArray.insert(0, newNode)
    return NodeHead

def travelByHead(head):
    while head:
        print head,head.val
        head = head.next

#用Array为了调试方便，链表题很容易弄乱结构，用Array可以保持住创建时的结构，变的只是里面的next
def travelByArray(array):
    for each in enumerate(array):
        try:
            print each[0],'point to:',each[1].next.pos
        except:
            print 'None'

#这个操作会改表头的
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
    global NodeHead
    NodeHead = curr
    return curr
    
    #比上面的写法多了一句话
    #if head == None or head.next == None:
    #    return head
    #curr = head
    #nextN = head.next
    #curr.next = None
    #while nextN:
    #    nextnext = nextN.next
    #    nextN.next = curr
    #    curr = nextN
    #    nextN = nextnext
    #global NodeHead
    #NodeHead = curr
    #return curr
    
if __name__ == '__main__':
    buildList(range(1,8))
    print NodeHead
    travelByHead(NodeHead)
    travelByArray(NodeArray)
    reverse_List(NodeHead)
    travelByHead(NodeHead)
    travelByArray(NodeArray)

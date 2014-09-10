
#coding:utf-8
class Node:
    def __init__(self,value):
        self.neigh = []
        self.value = value
        self.visited = False
        self.level = 1000
        self.father = []

    def isNeigh(self,other):#other is also Node
        if len(self.value) != len(other.value):
            return False
        count = 0
        for i in xrange(0,len(self.value)):
            if self.value[i] != other.value[i]:
                count+=1
        return count == 1

    def findNeigh(self, others):#others is a list of Node
        for each in others:
            if self.isNeigh(each):
                self.neigh.append(each)

class Solution:
    def __init__(self, start, end, dict):
        self.start = Node(start)
        self.end = Node(end)
        self.node_set = []
        self.node_set.append(self.start)# error occurs here
        self.node_set.append(self.end)
        self.start.level = 0

        for each in dict:
            self.node_set.append(Node(each))

    def buildMap(self):
        for each in self.node_set:
            each.findNeigh(self.node_set)

    path = []

    def trace(self,terminal):#need to be changed
        if len(terminal[0].father) == 0:
            print 'search end'
            print self.path
            return
        for each in terminal[0].father:
            self.path.append(each.value)
            self.trace([each])
            del self.path[-1]
        
    def ladderLength2(self, start, end):
        end_found = False
        self.buildMap()
        start.visited = True
        strQueue = []
        strQueue.append(start)
        while True:
            op = strQueue[0]
            del strQueue[0]
            if op.value == end.value: #从队列中取出时才看value
                self.path.append(end.value)
                self.trace([end])
                return
            for each in op.neigh:
                if op.level + 1 <= each.level:
                    each.level = op.level + 1
                    each.father.append(op)#这个节点可能已经被访问过了
                    if each.visited == False:
                        strQueue.append(each)
                    each.visited = True

if __name__ == '__main__':
    slu = Solution("hit", "cog", ["hot","dot","dog","lot","log"])
    slu.ladderLength2(slu.start,slu.end)

#encoding:UTF-8
import string
class Node:
    def __init__(self,value):
        self.neigh = []
        self.value = value
        self.visited = False
        self.level = 0
        self.father = None

    def isNeigh(self,other):#other is also Node
        if len(self.value) != len(other.value):
            return False
        count = 0
        for i in xrange(0,len(self.value)):
            if self.value[i] != other.value[i]:
                count+=1
        return count == 1

    def findNeigh(self, others):#others is a list of Node
        #for each in others:
        #    if self.isNeigh(each):
        #        self.neigh.append(each)
        length = len(self.value)
        alphabet = string.asciilowercase
        for i in range(0, length):
            for ch in alphabet:
                tmp_str = self.value(:i) + ch + self.value(i + 1:)
                if 

class Solution:
    def init(self, start, end, dict):
        self.start = Node(start)
        self.end = Node(end)
        self.node_set = set() 
        self.node_set.add(self.start)
        self.node_set.add(self.end)

        for each in dict:
            self.node_set.add(Node(each))

    #def buildMap(self, dict):# N^2 耗时建立map
    #    for each in dict:
    #        each.findNeigh(dict)

    def trace(self,terminal):
        curr = terminal
        ret_list = []
        while curr!= None:
            print curr.value
            ret_list.insert(0, curr.value)
            curr = curr.father
        return ret_list
        
    def ladderLength(self, start, end, dict):
        self.init(start,end,dict)
        #self.buildMap(self.node_set)
        strQueue = []
        strQueue.append(self.start)
        self.start.visited = True
        while True:
            try:
                op = strQueue[0]
                del strQueue[0]
            except:
                return 0
            if op.value == self.end.value: #bingo find end
                return op.level + 1
            op.find_neigh(self.node_set)
            for each in op.neigh:
                if each.visited == False:
                    each.visited = True
                    each.level = op.level + 1
                    each.father = op
                    strQueue.append(each)

if __name__ == '__main__':
    slu = Solution()
    print slu.ladderLength("hot", "dog", ["hot","dog"])
        

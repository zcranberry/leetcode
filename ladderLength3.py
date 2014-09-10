#from collections import deque
#from string import ascii_lowercase
#http://oj.leetcode.com/problems/word-ladder-ii/
class Solution:
    def ladderLength(self, start, end, dict):
        word_dict = {}
        maxLen = 2 ** 32
        for word in dict:
            word_dict[word] = maxLen
        word_dict[end] = maxLen
        word_dict[start] = 1
        word_queue = []
        word_queue.append(start)
        len_word = len(start)
        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        while True:
            try:
                curr = word_queue[0]
                del word_queue[0]
                #curr = word_queue.popleft()
                for i in range(0, len_word):
                    for ch in ascii_lowercase:
                        tmp = curr[:i] + ch + curr[i + 1:]
                        if tmp == end:
                        	return word_dict[curr] + 1
                        if tmp in word_dict:
                            if word_dict[tmp] > word_dict[curr] + 1:
                                word_dict[tmp] = word_dict[curr] + 1
                                word_queue.append(tmp)
            except:
                return 0

if __name__ == '__main__':
	slu = Solution()
	print slu.ladderLength('hit','cog',["hot","dot","dog","lot","log"])

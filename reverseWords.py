class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split()
        #print words
        #print len(words)
        #if len(words) == 0:
        #    print 'here'
        #    return ''
        return ' '.join(reversed(words))

if __name__ == '__main__':
    slu = Solution()
    print slu.reverseWords("   a   b ")

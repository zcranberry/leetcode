class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        
        mapped_str = map(extend_isalphanum, s)
        if len(mapped_str) == 0:
            return True
        ori_str = reduce(lambda x,y: x+y, mapped_str)
        if len(ori_str) < 1:
            return True
        #print ori_str
        rev_str = reduce(lambda x,y: x+y, list(reversed(ori_str)))
        return ori_str == rev_str


def extend_isalphanum(s):
    if s.isalnum():
        return s.lower()
    else:
        return ''

if __name__ == '__main__':
    #ori_str = reduce(lambda x,y: x+y, map(extend_isalphanum, 'A man, a plan, a canal: Panama'))
    #rev_str = reversed(ori_str)
    #print ori_str
    #print reduce(lambda x,y: x+y, list(rev_str))
    #print Solution().isPalindrome('A man, a plan, a canal: Panama')
    #print Solution().isPalindrome('race a car')
    print Solution().isPalindrome(' ')


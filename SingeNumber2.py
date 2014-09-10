#思路来自http://www.cnblogs.com/daijinqiao/p/3352893.html
#如果有三进制的表示，以及三进制的位运算，则很容易解决，现在使用二进制来模拟三进制
class Solution:
    # @param A, a list of integer
    # @return an integer
    def __init__(self, A):
        self.A = A
    def singleNumber(self, A):
        ones, twos, threes = [0, 0, 0]
        for each in A:
            twos |= (ones & each)
            ones ^= each
            threes = twos & ones
            twos &= (~threes)
            ones &= (~threes)
        return ones

if __name__ == '__main__':
    Slu = Solution([1,1,1,2])
    print Slu.singleNumber(Slu.A)

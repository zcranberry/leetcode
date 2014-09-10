class Solution:
    # @param A, a list of integer
    # @return an integer
    def __init__(self, A):
        self.A = A
    def singleNumber(self, A):
        ori = 0
        for each in A:
            ori = ori ^ each
        return ori

if __name__ == '__main__':
    Slu = Solution([1,1,2])
    print Slu.singleNumber(Slu.A)

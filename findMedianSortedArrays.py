#题目要求是log(m+n),复杂度，不过用(m+n)的算法居然也AC了
class Solution:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def findMedianSortedArrays(self, A, B):
        only = None
        if len(A) == 0:
            only = B
        elif len(B) == 0:
            only = A
        if only != None:
            return (only[(len(only) - 1) / 2] + only[len(only) / 2]) / 2.0 #奇偶位不用写if else

        full_length = len(A) + len(B)
        length = (full_length + 1)/ 2
        A.append(2.0 ** 1023)#哨兵位
        B.append(2.0 ** 1023)
        [pa, pb] = [0, 0]
        for i in range(0, length):
            if A[pa] < B[pb]:
                maxv = A[pa]
                pa += 1
            else:
                maxv = B[pb]
                pb += 1
            #print pa, pb
        if full_length % 2 == 1:
            return maxv / 1.0
        else:
            if A[pa] < B[pb]:
                maxv2 = A[pa]
            else:
                maxv2 = B[pb]
            return (maxv + maxv2) / 2.0

if __name__ == '__main__':
    Slu = Solution([],[1])
    print Slu.findMedianSortedArrays(Slu.A, Slu.B)
    Slu = Solution([1],[1])
    print Slu.findMedianSortedArrays(Slu.A, Slu.B)
    Slu = Solution([1],[2,3])
    print Slu.findMedianSortedArrays(Slu.A, Slu.B)
    Slu = Solution([1,3,5,7,9],[2,4,6,8])
    print Slu.findMedianSortedArrays(Slu.A, Slu.B)
    Slu = Solution([1,3,5,7,9],[2,4,6,8,10])
    print Slu.findMedianSortedArrays(Slu.A, Slu.B)

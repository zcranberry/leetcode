#encoding:UTF-8
#应该用组合数，如果对空间复杂度有要求
class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
        	return [1]
        tri = [[1]]
        for i in range(1, rowIndex + 1):
            row = [1]
            for j in range(1, i):
                row.append(tri[i - 1][j - 1] + tri[i - 1][j])
            row.append(1)
            tri.append(row)
        return tri[rowIndex]


#时间空间复杂度均为O(n)
class Solution2:
    def getRow(self, rowIndex):
        denominator = 1
        divisor = 1
        res = []
        for i in range(0, rowIndex + 1):
        	res.append(denominator / divisor)
        	denominator = denominator * (rowIndex - i)
        	divisor = divisor * (i + 1)
        return res

if __name__ == '__main__':
    for i in range(0, 7):
        print Solution2().getRow(i)

class Solution:
    def generate(self, numRows):
        if numRows == 0:
        	return []
        tri = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(tri[i - 1][j - 1] + tri[i - 1][j])
            row.append(1)
            tri.append(row)
        return tri

if __name__ == '__main__':
    print Solution().generate(1)
    print Solution().generate(2)
    print Solution().generate(3)
    print Solution().generate(4)
    print Solution().generate(5)
    print Solution().generate(6)

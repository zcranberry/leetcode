class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
        	return 0
        _min = 2 ** 32
        pro = 0
        for i in range(0,len(prices)):
        	pro = max(pro, prices[i] - _min)
        	_min = min(_min, prices[i])
        return pro

if __name__ == '__main__':
    print Solution().maxProfit([2,4,1])



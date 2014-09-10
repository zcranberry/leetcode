class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        pro = 0
        if len(prices) < 2:
        	return 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i - 1]:
            	pro += prices[i] - prices[i - 1]
        return pro
        
if __name__ == '__main__':
    print Solution().maxProfit([2,4,5,-1,1])

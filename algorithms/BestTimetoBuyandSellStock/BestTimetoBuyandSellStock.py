class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
    	if not prices:
    		return 0
    	temp = []
    	for i in range(1, len(prices)):
    		temp.append(prices[i] - prices[i - 1])
    	cur = res = 0
    	for i in temp:
    		cur = max(i, cur + i)
    		res = max(cur, res)
    	return res


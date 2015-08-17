class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
    	res = [[1]*n]*m
    	for i in range(1, m):
    		for i in range(1, n):
    			res[i][j] = res[i-1][j] + res[i][j-1]

    	return res[-1][-1]
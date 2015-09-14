class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum1(self, grid):
    	if not grid:
    		return None
    	m = len(grid)
    	n = len(grid[0])
    	res = [[0 for i in xrange(n)] for i in xrange(m)]
    	res[0][0] = grid[0][o]
    	for i in xrange(1 ,n):
    		res[0][i] += grid[0][i-1]
    	for j in xrange(1, m):
    		res[j][0] += res[j-1][0]
    	for i in range(1, n):
    		for j in range(1, m):
    			res[i][j] = min(res[i-1][j], res[i][j]) + grid[i][j]

    	return res[-1][-1]

    def minPathSum(self, grid):
    	if not grid:
    		return None
    	m , n = len(grid), len(grid[0])
    	for i in range(1, m):
    		grid[i][0] += grid[i-1][0]
    	for j in range(1, n):
    		grid[0][j] += grid[0][j-1]

    	for i in range(1, m):
    		for j in range(1, n):
    			grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    	return grid[-1][-1]
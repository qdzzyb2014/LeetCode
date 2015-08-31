class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
    	c1 = c2 = c3 = 0
    	for i in nums:
    		if 		i == 0: c1 += 1
    		elif 	i == 1: c2 += 1
    		else:			c3 += 1
    	nums[:c1] = [0]*c1
    	nums[c1:c1+c2] = [1]*c2
    	nums[c1+c2:] = [2]*c3
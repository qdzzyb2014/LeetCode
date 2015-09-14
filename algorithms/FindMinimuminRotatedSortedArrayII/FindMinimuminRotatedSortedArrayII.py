class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
    	return self.helper(nums, 0, len(nums)-1)

   	def helper(self, nums, l, r):
   		if l == r:
   			return nums[l]

   		mid = l + (r-l)/2
   		if nums[mid] > nums[r]:
   			return self.helper(nums, mid+1, r)
   		elif nums[mid] < nums[r]:
   			return self.helper(nums, l, mid)
   		else:
   			return self.helper(nums, l, r-1)
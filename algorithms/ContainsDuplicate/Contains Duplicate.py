class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate1(self, nums):
    	length = len(nums)
    	nums.sort()
    	for i in range(length):
    		if nums[i] == nums[i+1]:
    			return True
    	return False

    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)
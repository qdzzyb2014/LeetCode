class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
        	return
        j = -1
        for i in range(len(nums)):
        	if nums[i] == 0:
        		j += 1
        		nums[j], nums[i] = nums[i], nums[j]
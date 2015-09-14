class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo < hi:
        	if lo == hi:
        		return lo
        	mid = lo + (hi - lo) / 2
        	if nums[mid + 1] > nums[mid]:
        		lo = mid + 1
        	else:
        		hi = mid
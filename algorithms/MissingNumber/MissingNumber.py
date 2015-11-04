class Solution(object):
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)/2 - sum(nums)

    def missingNumber(self, nums):
        return reduce(operator.xor, nums+range(len(nums) + 1))

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        from collections import Counter
        c = Counter(nums)
        return [int(i) for i, n in c.items() if n == 1]

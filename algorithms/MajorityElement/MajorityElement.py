class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement1(self, nums):
        # 76ms
        from collections import Counter
        temp = dict(Counter(nums))
        for i in temp:
            if temp[i] > len(nums)/2:
                return i

    def majorityElement2(self, nums):
        # 72ms
        temp = set(nums)
        for i in temp:
            if nums.count(i) > len(nums)/2:
                return i

    def majorityElement3(self, nums):
        # 56ms
        nums.sort()
        return nums[len(nums)//2]

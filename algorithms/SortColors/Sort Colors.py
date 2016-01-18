class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors1(self, nums):
        c1 = c2 = c3 = 0
        for i in nums:
            if i == 0:
                c1 += 1
            elif i == 1:
                c2 += 1
            else:
                c3 += 1
        nums[:c1] = [0] * c1
        nums[c1:c1 + c2] = [1] * c2
        nums[c1 + c2:] = [2] * c3

    def sortColors(self, nums):
        zero = i = 0
        two = len(nums) - 1
        while i <= two:
            if nums[i] == 0:
                self._exchange(nums, i, zero)
                zero += 1
                i += 1
            elif nums[i] == 2:
                self._exchange(nums, i, two)
                two -= 1
            else:
                i += 1

    def exchange(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

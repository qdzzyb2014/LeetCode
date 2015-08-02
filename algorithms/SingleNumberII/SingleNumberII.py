class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        # 60ms
        from collections import Counter
        a, b = Counter(nums).most_common()[-1]
        return a

    def singleNumber1(self, nums):
        # 48ms
        nums.sort()
        for i in xrange(0, len(nums), 3):
            try:
                if nums[i] == nums[i+1] == nums[i+2]:
                    continue
                else:
                    return nums[i]
            except:
                return nums[i]

    def singleNumber2(self, nums):
        # 40ms
        return (sum(set(nums)) * 3 - sum(nums)) / 2
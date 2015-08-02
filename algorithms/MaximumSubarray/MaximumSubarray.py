class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for i in A[1:]:
            curSum = max(i, curSum+i)
            maxSum = max(curSum, maxSum)

        return maxSum

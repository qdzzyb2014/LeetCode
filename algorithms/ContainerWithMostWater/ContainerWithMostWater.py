class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        area = result = 0
        i, j = 0, len(height) - 1
        while i < j:
        	area = min(height[i], height[j]) * (j-i)
        	result = max(area, result)
        	if height[i] < height[j]:
        		i += 1
        	else:
        		j -= 1
        return result
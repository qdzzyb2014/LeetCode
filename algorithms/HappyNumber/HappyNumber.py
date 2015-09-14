class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
        	return True
        elif n == 4:
        	return False
        else:
        	res = 0
        	while n:
        		res += (n%10)**2
        		n = n/10
        	n = res
        	return self.isHappy(n)
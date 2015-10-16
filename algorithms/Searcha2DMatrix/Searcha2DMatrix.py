class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        top, right = 0, 0
        bottom, left = len(matrix)-1, len(matrix)-1
        tr = 0
        while top <= bottom:
            rmid = (bottom + top) / 2
            if target < matrix[rmid][0]:
                bottom = rmid - 1
            elif target > matrix[rmid][left]:
                top = rmid + 1
            else:
                tr = rmid

        while right <= left:
            cmid = (left + right) / 2
            if target < matrix[tr][cmid]:
                left = cmid - 1
            elif target > matrix[tr][cmid]:
                right = cmid + 1
            else:
                return True

        return False
                

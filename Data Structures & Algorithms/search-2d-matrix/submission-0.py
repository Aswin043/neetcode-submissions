class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top,bott = 0, rows - 1 
        while top <= bott:
            mr = (top + bott) // 2
            if target > matrix[mr][-1]:
                top = mr + 1
            elif target < matrix[mr][0]:
                bott = mr - 1
            else:
                break
            
        if not (top <= bott):
            return False
        row = (top + bott) // 2
        l,r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
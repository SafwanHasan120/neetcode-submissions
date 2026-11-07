class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        loRow = 0
        hiRow = len(matrix) - 1
        targetRow = -1
        while loRow <= hiRow:
            mid = (loRow + hiRow) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                targetRow = mid
                break
            elif matrix[mid][0] > target:
                hiRow = mid - 1
            else:
                loRow = mid + 1
        if targetRow == -1:
            return False
        
        loCol = 0
        hiCol = len(matrix[targetRow]) - 1
        while loCol < hiCol:
            mid = (loCol + hiCol) // 2
            if matrix[targetRow][mid] == target:
                return True
            if matrix[targetRow][mid] > target:
                hiCol = mid
            else:
                loCol = mid + 1
        return matrix[targetRow][loCol] == target
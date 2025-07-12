class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftM = 0
        rightM = len(matrix) - 1 

        while leftM <= rightM:
            middleM = ((rightM+leftM)//2)
            if (target > matrix[middleM][-1]):
                leftM = middleM + 1
            elif(target < matrix[middleM][0]):
                rightM = middleM - 1
            else:
                break
            
            
        left = 0
        right = len(matrix[middleM])

        while (left < right):
            middle = (left + right) // 2
            if matrix[middleM][middle] > target:
                right = middle
            elif matrix[middleM][middle] < target:
                left = middle + 1
            else:
                return True
        return False
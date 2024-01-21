class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        direction = 0
        num = 1
        result = []
        while (top <= bottom  and left <= right):
            if (direction == 0):
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                    num += 1
                top += 1
            elif (direction == 1):
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                    num += 1
                right -= 1
            elif (direction == 2):
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                    num += 1
                bottom -= 1
            elif (direction == 3):
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                    num += 1
                left += 1
            direction = (direction + 1) % 4
        
        return result
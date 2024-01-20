class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        largest = 0
        while (i < j):
            largest = max(largest, min(height[i], height[j]) * (j - i))

            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        
        return largest
        
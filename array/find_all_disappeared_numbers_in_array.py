class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            if (nums[index] < 0):
                pass
            else:
                nums[index] = -nums[index]
        
        return [i+1 for i, num in enumerate(nums) if num > 0]
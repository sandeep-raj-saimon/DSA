class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)

        last = None
        for i in range(n):
            if (nums[i] == last):
                return nums[i]
            else:
                last = nums[i]
        

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if (nums[abs(nums[i])] < 0):
                return abs(nums[i])
            
            nums[abs(nums[i])] = -nums[abs(nums[i])]
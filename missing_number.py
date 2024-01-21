class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return nums[len(nums)-1]+1

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        nums_sum = sum(nums)
        n = len(nums)
        actual_sum = n*(n+1)/2

        return int(actual_sum - nums_sum)
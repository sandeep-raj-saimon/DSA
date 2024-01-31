class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1
        last = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != last:
                nums[k] = nums[i]
                last = nums[i]
                k+=1
            else:
                pass
            
        return k
        
            
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 0

        for i in range(len(nums)):
            if (nums[i] == 0):
                nums[i] = -1

            if(i != 0):
                nums[i] = nums[i-1] + nums[i]


        m = {}
        max_len = 0
        for i in range(len(nums)):
            if m.get(nums[i]) is None:
                m[nums[i]] = i
            
            if (nums[i] == 0):
                max_len = max(max_len, i + 1)
            max_len = max(max_len, i - m[nums[i]])

        return max_len
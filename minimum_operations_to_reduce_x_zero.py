class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        if (sum(nums) < x):
            return -1

        left = []
        right = []
        left_sum = 0
        right_sum = 0

        left_dict = {}
        right_dict = {}
        left_dict[0]=0
        right_dict[0]=0
        n = len(nums)

        for i in range(len(nums)):
            left_sum += nums[i]
            left.append(left_sum)
            left_dict[left_sum] = i+1

            right_sum += nums[n-1-i]
            right.append(right_sum)
            right_dict[right_sum] = i+1
        
        ans = 999999
        for i in range(len(nums)):
            if (x-left[i]) in right_dict:
                ans = min(ans, right_dict[x-left[i]] + i + 1)
            else:
                pass

        for i in range(len(nums)):
            if (x-right[i]) in left_dict:
                ans = min(ans, left_dict[x-right[i]] + i + 1)
            else:
                pass
        
        if (ans == 999999):
            return -1
        return ans

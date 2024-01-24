class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        dict = {}
        dict[0] = 0
        ans = None
        for i in range(len(nums)):
            sum += nums[i]
            dict[sum] = i+1
            if sum - target in dict:
                if ans is None:
                    ans = dict[sum] - dict[sum-target]
                else:
                    ans = min(ans, dict[sum] - dict[sum-target])

        if ans is None:
            return 0
        else:
            return ans
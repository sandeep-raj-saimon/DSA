class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        ans = 0
        dic = defaultdict(int)
        arr = []
        
        for i in range(len(nums)):
            sum += nums[i]
            if (sum == k):
                ans+=1
           
            if sum - k in dic:
               ans += dic[sum-k]
            
            dic[sum]+=1
        return ans
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        last = nums[0]
        m = {}
        m[nums[0]]=1

        for i in range(1,len(nums)):
            if nums[i] not in m:
                m[nums[i]]=1
                nums[k]=nums[i]
                k+=1
                last = nums[i]
            else:
                value = m[nums[i]]
                if value == 1:
                    m[nums[i]] +=1
                    nums[k]=nums[i]
                    k+=1
                    last = nums[i]
                else:
                    pass
        return k

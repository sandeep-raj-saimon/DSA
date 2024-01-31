

from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        print(nums)
        m = {}
        n = {}

        l = len(nums)

        for i in range(l):
            target = -(nums[i])
            
            if (m.get(nums[i]) != None):
                pass
            else:
                m[nums[i]] = 1
                n = {}
                j = i + 1
                k = len(nums) - 1

                while(j < k):
                    b = n.get(nums[j])
                    c = n.get(nums[k])

                    if (nums[j] + nums[k] == target and (b == None and c == None)):
                        n[nums[j]] = 1
                        n[nums[k]] = 1
                        ans.append([nums[i], nums[j], nums[k]])
                        j += 1
                    elif (nums[j] + nums[k] > target):
                        k -= 1
                    else:
                        j += 1
            
        
        return ans

# the bruteforce approach would be to run 3 for loops and check for duplicate condition and the time complexity would be O(n^3)
# but if we sort the array, and use 2 pointer approach and then apply the duplicate check condition and it would have time complexity of O(n^2)
# the duplicate check condition is that:
# for a unique triplet, atleast one should be different, but as the question says, that the sum should be 0
# so we need to make sure that first element in triplet should not be same, we can use one global dictionary for this one
# and since other two elements can be different, we can use one local dictionary for these two elements
# and since sum of these two elements would be the negative of the third element, we can say that
# if the second element has been encountered before then the third element would have been encountered

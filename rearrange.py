class Solution:
    def rearrangeArray(self, nums):
        innercount = 1
        final = []
        final.append(nums[0])
        # final.append(nums[1])
        for i in range(1, len(nums)):
            temp = (nums[i]*2) - nums[i-1]
            for j in range(innercount, len(nums)):
                if temp != nums[j] and nums[j] not in final:
                    final.append(nums[j])
        return final

rearrange = Solution()

# print(rearrange.rearrangeArray([1,2,3,4,5]))
# print(rearrange.rearrangeArray( [6,2,0,9,7]))
print(rearrange.rearrangeArray( [1,2,3]))


                



        
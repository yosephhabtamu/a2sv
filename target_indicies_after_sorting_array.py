
class Solution:
    def targetIndices(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        return result

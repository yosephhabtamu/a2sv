class Solution:
    def moveZeroes(self, nums) -> None:

        j = -1
        # initial thought process
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        # print(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
        print(nums)


#  [0,1,0,3,12,]
solution = Solution()
solution.moveZeroes([0, 1, 0, 3, 12])

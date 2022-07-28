class Solution:
    def sort_func(self, num):
        frac =  (10 ** len(str(num)) - num )-1/(10 ** len(str(num)))
        print(num, frac)
        return frac 
    def largestNumber(self, nums):
        nums.sort(key = self.sort_func)
        nums2 = [str(i) for i in nums ]
        final = ''.join(nums2)
        # return final 
        print(final)
        
solution = Solution()
solution.largestNumber([111311, 1113])
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            counter = 0
            for j in nums:
                if i > j:
                    counter += 1
            result.append(counter)
        return result

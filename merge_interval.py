class Solution:
    def get_first(self, element):
        return element[0]

    def merge(self, intervals):
        result = []
        intervals.sort(key=self.get_first)
        result.append(intervals[0])
        intervals.pop(0)
        for i in intervals: 
            merger = False
            for j in result:
                if i[0] <= j[1]:
                    print(3)
                    temp = [i[0], i[1]] if i[1] >= j[1] else [i[0], j[1]]
                    result.remove(j)
                    result.append(temp)
                    merger = True
            if merger == False:
                result.append(i)
        return result


solution = Solution()
result = solution.merge([[15, 18], [1, 3], [8, 10], [2, 6]])
print(result)

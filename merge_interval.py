# class Solution:
#     def get_first(self, element):
#         return element[0]

#     def merge(self, intervals):
#         result = []
#         intervals.sort(key=self.get_first)
#         result.append(intervals[0])
#         intervals.pop(0)
#         for i in intervals:
#             merger = False
#             for j in result:
#                 if i[0] <= j[1]:
#                     print(3)
#                     temp = [i[0], i[1]] if i[1] >= j[1] else [i[0], j[1]]
#                     result.remove(j)
#                     result.append(temp)
#                     merger = True
#             if merger == False:
#                 result.append(i)
#         return result


class Solution:

    def get_first(self, interval):
        return interval[0]

    def merge(self, intervals):
        intervals.sort(key=self.get_first)
        print('sorted interval', intervals)
        result = [intervals[0]]

        def check_merge(j, i):
            return result[j][1] >= intervals[i][0]

        i = 1
        if len(intervals) == 1:
            return intervals
        else:
            while i < len(intervals):
                print(i)
                print(result[-1])
                if check_merge(-1, i):
                    result[-1][1] = result[-1][1]\
                         if result[-1][1] >= intervals[i][1]\
                         else intervals[i][1]

                    i += 1

                else:
                    result.append(intervals[i])
                    i += 1
        return result


solution = Solution()
result = solution.merge([[15, 18], [1, 3], [8, 10], [2, 6]])
print('result', result)

# for i in intervals:
#     # if temp == i:
#     #     continue
#     if temp[1] >= i[0]:
#         temp = temp if temp[1]>=i[1] else [temp[0],i[1]]
#         result.append(temp)
#     else:
#         temp = i
#         result.append(temp)


#  print(i, j)
#                 if i == len(intervals)-1:
#                     result.append(intervals[i])
#                     break
#                 elif i == len(intervals)-2 and check_merge(i, j) == False:
#                     result.append(intervals[i])
#                     result.append(intervals[j])
#                     break
#                 elif check_merge(i, j):
#                     result.append(intervals[i]
#                                   if intervals[i][1] > intervals[j][1]
#                                   else [intervals[i][0], intervals[j][1]])
#                     i += 2
#                     j += 2

#                 else:
#                     result.append(intervals[i])
#                     i += 1
#                     j += 1
#                 if i >= len(intervals):
#                     break

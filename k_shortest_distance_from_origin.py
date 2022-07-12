class Solution:
    def eculid (self,point:List[int]):
        return  point[0]**2 + point[1]**2
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x = len(points)
        #attempt one
        # for i in range(x):
        #     swapped = False
        #     for j in range(0, x-i-1):
        #         if points[j][0]**2 + points[j][1]**2  >  points[j+1][0]**2 + points[j+1][1]**2 :
        #             points[j], points[j+1] = points[j+1], points[j]
        #             swapped = True
        #     if swapped == False:
        #         break
        
        
        #attempt two
#         for i in range(len(points)):
#             for j in range(len(points)):
#                 if points[i][0] ** 2 + points[i][1] ** 2  <  points[j][0] ** 2 + points[j][1] ** 2 :
#                     points[i], points[j] = points[j], points[i]
       
        result = []
#         for i in range(k):
#             result.append(points[i])
#           
        #attempt three
        points.sort(key = self.eculid)
        for i in range(k):
            result.append(points[i])
            
        return result 
        
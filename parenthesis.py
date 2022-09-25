class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'{':'}', '(':')', '[':']'}
        ls = []
        ls.append(s[0])
        for i in s:
            for j in dict.keys():
                print(ls)
                if i == j:
                    ls.append(i)
                else:
                    temp = ls.pop()
                    if dict[temp] == i:
                        continue
                    else:
                        return False
        if ls == []:
            return True
        return False

                

solution=  Solution()
print(solution.isValid('[({})]'))
        
  
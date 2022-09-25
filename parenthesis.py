class Solution:
    def isValid(self, s):
        parenthesis = {'(': ')', '[': ']', '{': '}'}
        stack = []
        if len(s) == 1:
            return True if s[0] in parenthesis.keys() else False

        for i in range(len(s)):
            if s[i] in parenthesis.keys():
                stack.append(s[i])
            else:
                if stack !=[]:
                    temp = stack.pop() 
                else :
                    return False
                if parenthesis[temp] == s[i]:
                    continue
                else:
                    return False

        return True if stack == [] else False


solution = Solution()
print(solution.isValid(']('))

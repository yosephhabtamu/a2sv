
import math


class Solution:
    def evalRPN(self, tokens) -> int:
        operators = ['+','-', '*', '/']
        stack =[]
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            if i in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                if i == '+':
                    stack.append(num1+num2)
                elif i == '-':
                    stack.append(num2-num1)
                elif i == '*':
                    stack.append(num1*num2)
                else:
                    stack.append(math.trunc((num2/num1)))
        return stack[0]
solution = Solution()
solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        
        
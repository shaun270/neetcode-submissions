import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i.startswith('-') and i[1:].isdigit() or i.isdigit():
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                print(a,b)
                if i == '+':
                    stack.append(a+b)
                    
                elif i =='-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
                print(stack[-1])
        
        return int(stack[-1])
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        
        for token in tokens:
            if token == '+':
                res = int(stack.pop()) + int(stack.pop())
                stack.append(res)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                res = int(b) - int(a)
                stack.append(res)
            elif token == '*':
                res = int(stack.pop()) * int(stack.pop())
                stack.append(res)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                res = int(int(b) / int(a))
                stack.append(res)
            else:
                stack.append(token)
        return int(stack[0])





















































     
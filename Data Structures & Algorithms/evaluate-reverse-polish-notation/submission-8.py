class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '*', '-', '/']

        for operation in tokens:
            if operation == '+':
               res = (int(stack.pop()) + int(stack.pop()))
               stack.append(res)
            elif operation == '-':
                a = stack.pop()
                b = stack.pop()
                res = int(b) - int(a)
                stack.append(res)
            elif operation == '*':
                res = (int(stack.pop()) * int(stack.pop()))
                stack.append(res)
            elif operation == '/':
                a = stack.pop()
                b = stack.pop()
                res = int(b) / int(a)
                stack.append(res)
            else:
                stack.append(operation)

        return int(stack[0])
            
        
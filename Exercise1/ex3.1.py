# import sys

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def is_empty(self):
#         return len(self.items) == 0

#     def peek(self):
#         return self.items[-1]

# def evaluate_expression(expression):
#     tokens = expression.split()
#     stack = Stack()
#     num_operands_needed = 0
#     for token in tokens:
#         if token.isdigit():
#             stack.push(int(token))
#             num_operands_needed -= 1
#         elif token in ['+', '-', '*', '/']:
#             if token in ['+', '-', '*', '/']:
#                 num_operands_needed = 2
#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             result = None
#             if token == '+':
#                 result = operand1 + operand2
#             elif token == '-':
#                 result = operand1 - operand2
#             elif token == '*':
#                 result = operand1 * operand2
#             elif token == '/':
#                 result = operand1 / operand2
#                 if isinstance(operand1, int) and isinstance(operand2, int) and isinstance(result, float):
#                     result = int(result)
#             stack.push(result)
#             num_operands_needed -= 2
#         if num_operands_needed == 0:
#             num_operands_needed = 1
#     return stack.pop()

# if __name__ == '__main__':
#     expression = sys.argv[1]
#     result = evaluate_expression(expression)
#     print(result)
import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

def evaluate(expression):
    tokens = expression.split()
    stack = Stack()

    for token in tokens:
        if token == "+":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 + arg2)
        elif token == "-":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 - arg2)
        elif token == "*":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 * arg2)
        elif token == "/":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 / arg2)
        else:
            stack.push(int(token))

    return stack.pop()

if __name__ == "__main__":
    expression = sys.argv[1]
    result = evaluate(expression)
    print(result)

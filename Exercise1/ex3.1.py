import sys
import re

def evaluate_expression(expression):
    tokens = re.findall(r'\(|\)|[-+]?\d*\.\d+|\d+|[+\-*/]|\S+', expression)
    stack = []
    for token in tokens:
        if token == '(':
            continue
        elif token == ')':
            right_operand = stack.pop()
            left_operand = stack.pop()
            operator = stack.pop()
            if operator == '*':
                stack.append(left_operand * right_operand)
            elif operator == '/':
                stack.append(left_operand / right_operand)
            elif operator == '+':
                stack.append(left_operand + right_operand)
            elif operator == '-':
                stack.append(left_operand - right_operand)
            else:
                raise ValueError('Unknown operator: %s' % operator)
        elif token in ['*', '-', '+', '/']:
            stack.append(token)
        else:
            stack.append(int(token))
    result = stack.pop()
    if len(str(result)) == 3 and str(result)[-1] == "0":
        print(int(result))
    else:
        print(result)

expression = sys.argv[1]
evaluate_expression(expression)

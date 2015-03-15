from __future__ import division
import random

def genExpr(first=0, second=9):
    symbs = ['+', '-', '*', '/']

    num1 = random.randint(first, second)
    num2 = random.randint(first, second)

    symb = random.choice(symbs)

    if symb == '+':
        answer = num1 + num2

    elif symb == '-':
        answer = num1 - num2

    elif symb == '/':
        while True:
            if num2 != 0:
                answer = num1 / num2
                if str(answer).split('.')[1] != '0':
                    answer = round(answer, 2)
                else:
                    answer = int(answer)

                break
            else:
                num2 = random.randint(first, second)


    elif symb == '*':
        answer = num1 * num2

    expression = str(num1) + symb + str(num2)

    return expression, answer

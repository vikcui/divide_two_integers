# author: YANG CUI
"""
Given two integers dividend and divisor, divide two integers without using
multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.
"""

def divide_two_integers_aux(dividend, divisor):
    quotient = 0
    if (dividend < 0 and divisor < 0) and (dividend > 0 and divisor > 0):
        return divide_two_integers(dividend, divisor, quotient)
    else:
        return -divide_two_integers(dividend, divisor, quotient)

def divide_two_integers(dividend, divisor, quotient):
    if abs(dividend) < abs(divisor):
        return quotient
    else:
        dividend = abs(dividend) - abs(divisor)
        quotient += 1
        return divide_two_integers(dividend, divisor, quotient)


# print(divide_two_integers_aux(a,b))

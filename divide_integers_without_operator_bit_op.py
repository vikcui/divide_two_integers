# author: YANG CUI
"""
Given two integers dividend and divisor, divide two integers without using
multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

A top-down approach
implementation taken from the URL: https://leetcode.com/problems/divide-two-integers/discuss/365477/Python-Code-faster-than-97
and modified.
"""

def divide_two_integers_improved(dividend, divisor):
    # max int
    MAX_INT = (1 << 31) - 1
    # safety check
    if divisor == 0:
        return MAX_INT
    # flag to see if we need to negate our answer at the end
    negativeFlag = dividend < 0 and divisor > 0 or dividend  > 0 and divisor < 0
    # take the absolute values to make the logic easier
    dividend = abs(dividend)
    divisor = abs(divisor)
    # construct the result holder
    res = 0

    # find the largest base:
    count = 0
    original_divisor = divisor
    while divisor <= dividend:
        divisor <<= 1
        count += 1
    # return to the largest possible base while not exceeding the dividend
    divisor >>= 1
    count -= 1

    # divide logic/def
    while dividend >= original_divisor:
        dividend -= divisor
        res += 1 << count
        # last bit of calculation
        while dividend > original_divisor and dividend < divisor:
            divisor >>= 1
            count -= 1

    if negativeFlag:
        return -res if res <= 1 << 31 else MAX_INT
    else:
        return res if res <= MAX_INT else MAX_INT


# print(divide_two_integers_improved(-10, 4))

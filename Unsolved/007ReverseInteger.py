"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x = (-x)

        nums = []
        while x >= 1:
            nums.append(x % 10)
            x = x / 10

        inversed_integer = 0
        a = len(nums) - 1
        for n in nums:
            inversed_integer += n * (10 ** a)
            a -= 1

        if negative:
            inversed_integer = (-inversed_integer)

        return inversed_integer
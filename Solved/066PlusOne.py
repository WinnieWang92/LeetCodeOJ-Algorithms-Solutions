"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        num = 0
        max_num = 0
        new_l = l

        for i in range(l):
            j = l - i - 1
            num += digits[i] * (10 ** j)
            max_num += 9 * (10 ** j)

        if num == max_num:
            new_l = l + 1
        num += 1

        new_digits = []
        for i in range(1, new_l + 1):
            d = num % 10
            new_digits.append(d)
            num /= 10
        new_digits.reverse()

        return new_digits

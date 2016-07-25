"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97

I 1, V 5, X 10, L 50, C 100, D 500, M 1000
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        val_list = [1, 5, 10, 50, 100, 500, 1000]
        d = {}
        for i in range(7):
            d[key_list[i]] = val_list[i]

        int_l = []
        for c in s:
            int_l.append(d[c.upper()])

        new_l = int_l[:]

        # minus first
        for i in range(len(int_l)-1):
            if int_l[i] < int_l[i+1]:
                new_l[i] = int_l[i+1] - int_l[i]
                new_l[i+1] = 0

        # then sum up
        sum = 0
        for t in new_l:
            sum += t

        return sum

s = 'MCMXCVI'
solution = Solution()
print solution.romanToInt(s)
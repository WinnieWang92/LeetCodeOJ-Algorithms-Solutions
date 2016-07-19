"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".


"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        rl= list(reversed(l))
        r_str=''.join(rl)
        return r_str
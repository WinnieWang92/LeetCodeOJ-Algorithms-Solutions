"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        result = False
        if x < 2147483647 and str(x) == str(x)[::-1]:
            result = True

        return result


x = -2147447412
solution = Solution()
print solution.isPalindrome(x)

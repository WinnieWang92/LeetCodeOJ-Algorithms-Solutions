"""
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

"""


class Solution(object):
    def listToStr(self, l):
        string = ''
        for c in l:
            string += str(c)
        return string

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        max_res_length = 0
        res = ''

        if len(l) <= 2 and l[0] == l[len(l)-1]:
            res = self.listToStr(l)
        else:
            for i in range(1, len(l)):
                max_search = min(i, len(l)-1-i)
                search = 1
                l1 = []
                l2 = []
                l2.append(l[i])
                while search <= max_search and l[i-search] == l[i+search]:
                    l1.append(l[i-search])
                    l2.append(l[i+search])
                    search += 1

                length = len(l1)*2+1
                if length > max_res_length:
                    max_res_length = length
                    res = self.listToStr(reversed(l1)) + self.listToStr(l2)

        return res


s = 'abb'
# ying gai shi 'bb'
solution = Solution()
print solution.longestPalindrome(s)

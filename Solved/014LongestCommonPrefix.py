"""
Write a function to find the longest common prefix string amongst an array of strings
"""


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''
        else:
            flag = 1
            shortest_str = min(strs, key=len)
            i = 0
            while i < len(shortest_str) and flag == 1:
                for s in strs:
                    if s[i] != shortest_str[i]:
                        flag = 0
                        break
                if flag == 0:
                    break
                else:
                    i += 1

            return shortest_str[0:max(i, 0)]



strs = ['ac', 'ac', 'a']
solution = Solution()
print solution.longestCommonPrefix(strs)


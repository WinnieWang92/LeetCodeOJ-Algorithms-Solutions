"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(s)
        maxlength = 1

        for i in range(len(l) - 1):
            char_set = set()
            char_set.add(l[i])
            j = i + 1

            while (j < len(l) and l[j] not in char_set):
                char_set.add(l[j])
                j += 1
            maxlength = max(maxlength, len(char_set))

        if s == '':
            return 0
        else:
            return maxlength


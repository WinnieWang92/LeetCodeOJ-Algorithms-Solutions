"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lefts = ['(', '[', '{']
        rights = [')', ']', '}']
        d = {}
        for i in range(3):
            d[lefts[i]] = rights[i]

        brackets = ['(', '[', '{', ')', ']', '}']
        res = True

        if len(s) % 2 == 1:
            res = False
            print 1
        else:
            d_index = {}
            for bracket in brackets:
                array = []
                for i in range(len(s)):
                    if bracket == s[i]:
                        array.append(i)
                d_index[bracket] = array

            for left in lefts:
                left_indexes = d_index[left][:]
                right = d[left]
                right_indexes = d_index[right][:]

                if len(left_indexes) != len(right_indexes):
                    res = False
                    print 2
                    break
                else:
                    for i in range(len(left_indexes) - 1, -1, -1):
                        li = left_indexes[i]
                        min_dist = max(right_indexes)
                        nearest_ri = right_indexes[0]

                        # find nearest right bracket
                        for j in range(len(right_indexes)):
                            ri = right_indexes[j]
                            dist = ri - li
                            if 0 < dist < min_dist:
                                min_dist = dist
                                nearest_ri = ri

                        if (nearest_ri - li) % 2 == 0:
                            res = False
                            break
                        else:
                            left_indexes.remove(li)
                            right_indexes.remove(nearest_ri)
        return res

s = '}}(]}}){)(])](}{{}[]'
solution = Solution()
print solution.isValid(s)

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        slist = list(s)
        new_s = ''
        lists = [[] for row in range(numRows)]
        line = 0
        step = 1

        for c in slist:
            lists[line].append(c)
            next_line = line + step
            if next_line == numRows:
                step = -1
            if next_line < 0:
                step = 1
            line += step

        for l in lists:
            for c in l:
                new_s += str(c)
        return new_s
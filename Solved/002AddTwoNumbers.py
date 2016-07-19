"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_num = 0
        l2_num = 0
        i = 0
        j = 0

        while l1 is not None:
            l1_num += l1.val * (10 ** i)
            i += 1
            l1 = l1.next

        while l2 is not None:
            l2_num += l2.val * (10 ** j)
            j += 1
            l2 = l2.next

        sum_num = l1_num + l2_num
        sum_list = []
        if sum_num == 0:
            sum_list.append(0)
        else:
            while sum_num != 0:
                sum_list.append(sum_num % 10)
                sum_num = sum_num / 10

        ls = None
        for s in range(len(sum_list) - 1, -1, -1):
            new_node = ListNode(sum_list[s])
            new_node.next = ls
            ls = new_node
        return ls

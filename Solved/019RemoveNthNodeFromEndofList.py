"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next

        l.pop(-n)

        l_res = None
        for i in range(len(l) - 1, -1, -1):
            new_node = ListNode(l[i])
            new_node.next = l_res
            l_res = new_node
        return l_res



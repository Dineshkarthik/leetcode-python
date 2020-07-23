"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def _get_list(list_node: ListNode) -> List[str]:
            list_: list = []
            while list_node:
                list_.append(str(list_node.val))
                list_node = list_node.next
            return list_[::-1]

        def _get_list_node(list_):
            if len(list_) == 1:
                return ListNode(int(list_[0]))
            return ListNode(int(list_[0]), _get_list_node(list_[1:]))

        list1: list = _get_list(l1)
        list2: list = _get_list(l2)
        sum_ = int("".join(list1)) + int("".join(list2))
        return _get_list_node(list(str(sum_))[::-1])


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1: list = []
        list2: list = []
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next
        sum_list = list(
            str(int("".join(list1[::-1])) + int("".join(list2[::-1])))
        )[::-1]
        temp_head = ListNode(-1)
        head = ListNode(sum_list[0])
        temp_head.next = head
        for i in range(1, len(sum_list)):
            node = ListNode(sum_list[i])
            head.next = node
            head = head.next
        return temp_head.next


### Test cases


def get_list(list_node: ListNode) -> List[str]:
    list_: list = []
    while list_node:
        list_.append(int(list_node.val))
        list_node = list_node.next
    return list_


s = Solution()

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
assert get_list(s.addTwoNumbers(l1, l2)) == [7, 0, 8]

l1 = ListNode(1, ListNode(8))
l2 = ListNode(0)
assert get_list(s.addTwoNumbers(l1, l2)) == [1, 8]

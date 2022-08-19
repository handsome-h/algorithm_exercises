"""
输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
"""


class ListNode:
    """
    链表结点
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# 3, 1, 4, 2, 5
pHead = ListNode(3, ListNode(1, ListNode(4, ListNode(2, ListNode(5)))))


def print_list_reversingly(pNode):
    if pNode is None:
        return

    print_list_reversingly(pNode.next)

    print(pNode.data)
    

print_list_reversingly(pHead)

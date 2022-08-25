"""
定义一个函数，输入一个链表的头结点，反转该链表并输入反转后链表的头结点。
"""


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


list_head = ListNode(3, ListNode(5, ListNode(2, ListNode(1, ListNode(4)))))


def reverse_list(head):
    reversed_head = None
    node = head
    prev = None

    while node is not None:
        next = node.next

        if next is None:
            reversed_head = node

        node.next = prev

        prev = node
        node = next

    return reversed_head


a = reverse_list(list_head)
print(a.val)
print(a.next.val)

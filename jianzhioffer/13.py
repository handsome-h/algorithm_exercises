"""
给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该结点。链表结点与函数的定义如下：
"""


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def delete_node(list_head: ListNode, to_be_deleted: ListNode):
    if not(list_head and to_be_deleted):
        return

    if to_be_deleted.next is not None:
        p_next: ListNode = to_be_deleted.next
        to_be_deleted.val = p_next.val
        to_be_deleted.next = p_next.next
        del p_next

    # 链表只有一个结点，删除头结点（也是尾结点）
    elif list_head == to_be_deleted:
        del to_be_deleted
    # 链表中有多个结点，删除尾结点
    else:
        p_node = list_head
        while p_node.next != to_be_deleted:
            p_node = p_node.next

        p_node.next = None
        del to_be_deleted


to_be_deleted = ListNode(4)
# list_head = ListNode(3, ListNode(5, ListNode(2, ListNode(1, to_be_deleted))))
list_head = None
delete_node(list_head, to_be_deleted)
print(list_head.val)
print(list_head.next.val)
print(list_head.next.next.val)
print(list_head.next.next.next.val)
print(list_head.next.next.next.next.val)

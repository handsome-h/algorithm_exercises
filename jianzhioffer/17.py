"""
输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的。
"""


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


list1_head = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))
list2_head = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))


def merge(head1: ListNode, head2: ListNode):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    merge_head = None
    if head1.val <= head2.val:
        merge_head = head1
        merge_head.next = merge(head1.next, head2)
    else:
        merge_head = head2
        merge_head.next = merge(head1, head2.next)

    return merge_head


merge_head = merge(list1_head, list2_head)
cur = merge_head
while cur:
    print(cur.val)
    cur = cur.next

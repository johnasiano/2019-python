def mergeTwoLists1(self, l1, l2):
    pre = temp = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    temp.next = l1 or l2
    return pre.next

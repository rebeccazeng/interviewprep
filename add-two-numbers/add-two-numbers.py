# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLink(self, head):
        curr = head
        prev = None
        next = None
        # reverse the second list
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total = None
        # l2 = self.reverseLink(l2)
        # add together the two lists
        carry_over = 0
        while l1 is not None or l2 is not None:
            addition = 0
            if carry_over > 0:
                addition += carry_over
                carry_over = 0
            if l1 is None:
                addition += l2.val
                l2 = l2.next
            elif l2 is None:
                addition += l1.val
                l1 = l1.next
            else:
                addition += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            # now to create the linked list
            if addition < 9:
                total = ListNode(addition, total)
            else:
                carry_over = addition // 10
                addition = addition % 10
                total = ListNode(addition, total)
        if carry_over > 0:
            total = ListNode(carry_over, total)
        return self.reverseLink(total)

            
            
            
        
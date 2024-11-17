# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        borrow = 0
        sumL = ListNode()
        cur_s = sumL
        num = 0
        while cur1 != None and cur2 != None:
            num += 1
            sum = cur1.val + cur2.val + borrow
            borrow = sum // 10
            cur_s.next = ListNode()
            cur_s = cur_s.next
            cur_s.val = sum%10
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1 != None:
            sum = cur1.val + borrow
            borrow = sum // 10
            cur_s.next = ListNode()
            cur_s = cur_s.next
            cur_s.val = sum%10
            cur1 = cur1.next
        while cur2 != None:
            sum = cur2.val + borrow
            borrow = sum // 10
            cur_s.next = ListNode()
            cur_s = cur_s.next
            cur_s.val = sum%10
            cur2 = cur2.next
        if borrow == 1:
            cur_s.next = ListNode()
            cur_s = cur_s.next
            cur_s.val = 1

        return sumL.next


        

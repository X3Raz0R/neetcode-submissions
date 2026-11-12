# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next
        numar1=0
        numar2=0
        while stack1:
            numar1 = numar1*10+stack1.pop()
        while stack2:
            numar2=numar2*10+stack2.pop()
        numarf = numar1+numar2
        if numarf == 0:
            return ListNode(0)
        dummy = ListNode()
        cur = dummy
        while numarf>0:
            cur.next = ListNode(numarf%10)
            cur = cur.next
            numarf//= 10
        return dummy.next



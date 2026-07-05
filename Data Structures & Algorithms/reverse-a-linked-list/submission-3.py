# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listanoua = None
        current = head
        while current:
            nodurm = current.next
            current.next = listanoua
            listanoua = current
            current = nodurm

        return listanoua
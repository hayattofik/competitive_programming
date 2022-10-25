# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur=head
        dummy=ListNode(next=head)
        prev=dummy
        while cur :
            nxt=cur.next
            if cur.val==val:
                prev.next=nxt
            else:
               prev=cur
            cur=cur.next
        return dummy.next
                
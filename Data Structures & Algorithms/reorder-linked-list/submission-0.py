# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_list(self,head):
        prev=None
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        l1=head
        l2=slow.next
        slow.next=None
        l2=self.reverse_list(l2)

        while l1 and l2:
            n1=l1.next
            n2=l2.next
            l1.next=l2
            l2.next=n1
            l1=n1
            l2=n2
